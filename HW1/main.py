import sys
from shell import Shell

def main():
    if len(sys.argv) != 4:
        print("Usage: python main.py <hostname> <tar_path> <start_script>")
        sys.exit(1)

    hostname = sys.argv[1]
    tar_path = sys.argv[2]
    start_script = sys.argv[3]

    shell = Shell(hostname, tar_path, start_script)
    shell.run()

if __name__ == "__main__":
    main()