import json
import matplotlib.pyplot as plt
import sys
import time
import threading
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

TEMPLATE_WIDTH = 1404
TEMPLATE_HEIGHT = 1872
font_scale = 0.28

def evaluate(expr, variables):
    if isinstance(expr, (int, float)):
        return expr
    if isinstance(expr, str):
        try:
            return eval(expr, {}, variables)
        except Exception as e:
            print(f"Eval error for: {expr} -> {e}")
            return 0
    return 0

def draw_path(ax, path_data, variables, style=None):
    i = 0
    while i < len(path_data):
        if path_data[i] == "M":
            x1 = evaluate(path_data[i+1], variables)
            y1 = evaluate(path_data[i+2], variables)
            x2 = evaluate(path_data[i+4], variables)
            y2 = evaluate(path_data[i+5], variables)
            ax.plot([x1, x2], [y1, y2], **(style or {}))
            i += 6
        elif path_data[i] == "Z":
            i += 1
        else:
            i += 1

def render_template(ax, template):
    ax.clear()
    ax.set_xlim(0, TEMPLATE_WIDTH)
    ax.set_ylim(TEMPLATE_HEIGHT, 0)
    ax.set_aspect('equal')
    ax.axis('off')

    variables = {
        "templateWidth": TEMPLATE_WIDTH,
        "templateHeight": TEMPLATE_HEIGHT
    }

    if "constants" in template:
        for const in template["constants"]:
            for k, v in const.items():
                variables[k] = evaluate(v, variables)

    for item in template.get("items", []):
        if item["type"] == "path":
            style = {
                "linewidth": item.get("strokeWidth", 1),
                "color": item.get("strokeColor", "#000000")
            }
            draw_path(ax, item["data"], variables, style)

        elif item["type"] == "text":
            x = evaluate(item["position"]["x"], variables)
            y = evaluate(item["position"]["y"], variables)
            ax.text(x, y, item["text"],
                    fontsize=item.get("fontSize", 12) * font_scale,
                    va="top", ha="left",
                    color="black")

class TemplateWatcher(FileSystemEventHandler):
    def __init__(self, path, fig, ax):
        self.path = path
        self.fig = fig
        self.ax = ax
        self.last_reload = 0

    def on_modified(self, event):
        if event.src_path.endswith(self.path):
            # debounce reloads
            if time.time() - self.last_reload < 0.5:
                return
            self.last_reload = time.time()
            try:
                with open(self.path) as f:
                    template = json.load(f)
                render_template(self.ax, template)
                self.fig.canvas.draw()
                print("Template reloaded.")
            except Exception as e:
                print(f"Failed to reload template: {e}")

def live_preview(template_file, interval=2):
    plt.rcParams["figure.facecolor"] = "none"
    fig, ax = plt.subplots(figsize=(7, 9.4), facecolor='none')
    ax.set_facecolor("none")
    fig.canvas.manager.set_window_title("Template Preview")

    print(f"🔁 Reloading every {interval} seconds...")

    while True:
        try:
            with open(template_file) as f:
                template = json.load(f)
            render_template(ax, template)
            fig.tight_layout()
            fig.canvas.draw()
            fig.canvas.flush_events()
        except Exception as e:
            print(f"⚠️ Error loading template: {e}")
        plt.pause(interval)
        
        
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python preview_template.py <template_file.json>")
        sys.exit(1)

    template_file = sys.argv[1]
    live_preview(template_file)
