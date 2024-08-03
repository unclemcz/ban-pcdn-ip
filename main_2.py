import ipaddress
import sys

def cidr_to_range(cidr):
    network = ipaddress.ip_network(cidr)
    return (network.network_address, network.broadcast_address)

def range_to_cidr(start, end):
    return [str(cidr) for cidr in ipaddress.summarize_address_range(start, end)]

def merge_cidrs(cidrs):
    ranges = sorted(cidr_to_range(cidr) for cidr in cidrs)
    merged = []
    for start, end in ranges:
        if not merged or start > merged[-1][1] + 1:
            merged.append([start, end])
        else:
            merged[-1][1] = max(merged[-1][1], end)
    
    result = []
    for start, end in merged:
        result.extend(range_to_cidr(start, end))
    return result

def main():
    print("请输入IP段列表（每行一个CIDR格式的IP段）:")
    print("输入完成后，请按Ctrl+D (Unix/Linux/Mac) 或 Ctrl+Z 然后按Enter (Windows) 来结束输入")
    
    input_cidrs = []
    for line in sys.stdin:
        cidr = line.strip()
        try:
            ipaddress.ip_network(cidr)
            input_cidrs.append(cidr)
        except ValueError:
            print(f"无效的CIDR格式: {cidr}，已忽略", file=sys.stderr)

    if not input_cidrs:
        print("未输入有效的IP段", file=sys.stderr)
        return

    merged_cidrs = merge_cidrs(input_cidrs)

    print("\n合并后的IP段:")
    for cidr in merged_cidrs:
        print(cidr)

if __name__ == "__main__":
    main()
