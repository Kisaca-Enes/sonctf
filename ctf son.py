yaz = input("hos geldin bakalim neler yapicaksin: ")
print("kullanabilcehin komutlar")

packet = """Frame 1: 74 bytes on wire (592 bits), 74 bytes captured (592 bits)
    Arrival Time: May 7, 2025 16:04:38.898054000 UTC
    Time delta from previous packet: 0.000000000 seconds
    Frame Number: 1
    Packet Length: 74 bytes
    Capture Length: 74 bytes
    Protocols in frame: eth:ip:icmp
Ethernet II, Src: 00:14:22:01:23:45 (00:14:22:01:23:45), Dst: 00:14:22:01:23:46 (00:14:22:01:23:46)
    Destination: 00:14:22:01:23:46 (00:14:22:01:23:46)
    Source: 00:14:22:01:23:45 (00:14:22:01:23:45)
    Type: IPv4 (0x0800)
Internet Protocol Version 4, Src: 192.168.1.1, Dst: 192.168.1.2
    Version: 4
    Header Length: 20 bytes
    Total Length: 60 bytes
    Identification: 0x1a2b (6699)
    Flags: 0x00
    Time to live: 64
    Protocol: ICMP (1)
    Header checksum: 0xb1e7 [correct]
    Source: 192.168.1.1
    Destination: 192.168.1.2
    Options: (0 bytes)
Internet Control Message Protocol
    Type: 8 (Echo Request)
    Code: 0
    Checksum: 0xd1f0 [correct]
    Identifier (PID): 0x1a2b
    Sequence Number: 1
    Data (32 bytes)
        Data: 0x48656c6c6f20576f726c64
        [Length: 32]
"""
vuln = "kernel tabanli staxk owrflow var gbd ./vuln ile bak "
m = """""4d65726861626120656e65732062656e206b61c3a720736161746c6572696e64652062696c6d69796f72756d20616d612062752062697220696e7461686172206d656b74756275206861796174696d6120736f6e72207665726d65206b61726172c4b120616c64c4b16d2065c49f6572207961706162696c697273656d2062656e696d2069c3a7696e207a6f722062697220646f6e656d20626972206b61c3a72064616d6c6179616e207665207461c59f616e2064616d6c612062617a69206475796d616d6120676572656b656e20c59f65796c657269206475796d616d2076622062756e6c61722065746b692065746920616d612073616ec4b172c4b16d2079657465722064616861206461206b6174616c616e616d697963616d20736f6e20637466206d6920636f7a6475737567756e2069c3a7696e20c3a76f6b207465c59f656b6bc3bc726c6572206f6c616e20686f63616d2062616e6120c3a76f6b20c59f6579206f67726574696e697a20756d6172c4b16d206861796174c4b16ec4b17a646120c3a76f6b2069796920c59f65796c65722062617361726973696e697a2073697a646520616e74692064656269616e20766520617274726f6a616e20686f63616d20686570696e697a6920c3a76f6b2073657669796f72756d2062656e69207a6f7262616c616d61646967696e697a20766520676572c3a7656b74656e2061726b616461c59f206f6c6475c49f756e757a2069c3a7696e20c3a76f6b2074657373656b75722065646572696d"""
if yaz == "nmap":
    print("server is closed but 1 pc is oppenet")
elif yaz == "wireshark":
    print(f"packet: {packet}")
elif yaz == "nmap" and "192.168.1.2":
    print("opened 22 3389 80 3306 445")
elif yaz == "http://192.168.1.2":
    print("welcome web site: 1: report bug 2 search folder 3 login 4 users")
    choice = input("Enter your choice: ")
    if choice == "1":
        print("./report.text")
    elif choice == "2":
        print("searching folders...")
    elif choice == "3":
        print("login successful")
    elif choice == "4":
        print("users found")
elif yaz == "report":
    print("admin cookie: A.DMin")
elif yaz == "cookie: A.DMin":
    print("welcome mark upload folder firewall rule")
elif yaz == "upload":
    print("upload the shell.php")
elif yaz == "firewallrule":
    print("rule: opened unknown network: blocked")
elif yaz == "close":
    print("firewall closed")
else:
    print("shell nasil almayi dusunuyorsun")

if yaz == "http://192.168.1.2/shell.php":
    print("welcome to the system")
elif yaz == "ls":
    print("data")
elif yaz == "cd data":
    print("21 port = 212121")
elif yaz == "ftp" and "212121":
    print("welcome system")
    if yaz == "ls":
        print("info.txt")
    elif yaz == "cat info.txt":
        print("sql server version: MySQL 3.x – 4.0.x")
    elif yaz == "meterpreter":
        print("sql exploit")
        if yaz == "set sqlexploit":
            print("calisma basladi")
            print("pyload deneniyor")
            time.sleep(5)
            print("basarili shell alindi")
            if yaz == "ls":
                print("database.bs")
            elif yaz == "cat database.bs":
                print("1 5 16 12 8 2 8 2 8 2")
            elif yaz == "rdesktop 192.168.1.2 -u mark -p admin82":
                print("welcome mark")
                if yaz == "ls":
                    print("program.c")
                elif yaz == "cat program.c":
                    print(vuln)
                    if yaz == "gdb ./vuln":
                        print("0xdeadbeef")
                        print("exploit yazimina usendim root sun tebeikler simdi son mektubumu oku hersey icin tesekurler")
                        print("cat mektup.txt once hex yani base 16")
                        print(m)
