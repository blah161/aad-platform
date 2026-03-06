from flask import Flask, render_template
import os
import importlib

app = Flask(__name__)

TOOLS = []

tools_dir = "tools"

if os.path.exists(tools_dir):
for tool in os.listdir(tools_dir):

    if tool.startswith("."):
        continue
        module_path = f"tools.{tool}.routes"

        module = importlib.import_module(module_path)

        blueprint = getattr(module, tool)

        app.register_blueprint(blueprint, url_prefix=f"/{tool}")

        TOOLS.append({
            "name": tool.capitalize(),
            "path": f"/{tool}"
        })


@app.route("/")
def dashboard():
    return render_template("dashboard.html", tools=TOOLS)
