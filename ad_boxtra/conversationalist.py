import datetime
import socket

def main():
    print("+----------------------------------------------------------------------------------+")
    print("|             👋 Hello! My name is Ad Boxtra, the boxy rover from NIU.             |")
    print("|                                                                                  |")
    print("|                  ⌚ It is currently", datetime.datetime.now(),"                  |")
    print("|                                                                                  |")
    print("|                            🌐 My IP is", socket.gethostbyname(socket.gethostname()),"                               |")
    print("|                                                                                  |")
    print("|             If you want to know more about how to make me do things,             |")
    print("|                  check out https://github.com/NIURoverTeam/Docs                  |")
    print("|                                                                                  |")
    print("| You can help build me at https://niurover.com or https://github.com/NIURoverTeam |")
    print("+----------------------------------------------------------------------------------+")

if __name__ == '__main__':
    main()
