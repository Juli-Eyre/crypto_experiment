##尝试用词频分析写了一下午..
from string import ascii_letters, digits

# find_index_key: 确定key中index部分ascii码
# sub_arr: 当key_len和index确定时,使用key中同一位加密的子串
# 返回该子串可能使用的所有可见字符
def find_index_key(sub_arr):  # sub_arr是同一个ki的分组
    # all_ch = printable
    all_key = ascii_letters + digits + ',' + '.' + ' '
    test_key = []
    possible_key = []
    # 遍历整个ascii码(0-127)
    for x in range(0x00, 0xFF):
        test_key.append(x)
        possible_key.append(x)
    # 如果子串中所有位置都可以被ch异或为可见字符,则该ch可能为key的一部分
    for i in test_key:
        for j in sub_arr:
            if chr(i ^ j) not in all_key:
                possible_key.remove(i)
                break
    return possible_key

s = "F96DE8C227A259C87EE1DA2AED57C93FE5DA36ED4EC87EF2C63AAE5B9A7EFFD673BE4ACF7BE8923CAB1ECE7AF2DA3DA44FCF7AE29235A24C963FF0DF3CA3599A70E5DA36BF1ECE77F8DC34BE129A6CF4D126BF5B9A7CFEDF3EB850D37CF0C63AA2509A76FF9227A55B9A6FE3D720A850D97AB1DD35ED5FCE6BF0D138A84CC931B1F121B44ECE70F6C032BD56C33FF9D320ED5CDF7AFF9226BE5BDE3FF7DD21ED56CF71F5C036A94D963FF8D473A351CE3FE5DA3CB84DDB71F5C17FED51DC3FE8D732BF4D963FF3C727ED4AC87EF5DB27A451D47EFD9230BF47CA6BFEC12ABE4ADF72E29224A84CDF3FF5D720A459D47AF59232A35A9A7AE7D33FB85FCE7AF5923AA31EDB3FF7D33ABF52C33FF0D673A551D93FFCD33DA35BC831B1F43CBF1EDF67F0DF23A15B963FE5DA36ED68D378F4DC36BF5B9A7AFFD121B44ECE76FEDC73BE5DD27AFCD773BA5FC93FE5DA3CB859D26BB1C63CED5CDF3FE2D730B84CDF3FF7DD21ED5ADF7CF0D636BE1EDB79E5D721ED57CE3FE6D320ED57D469F4DC27A85A963FF3C727ED49DF3FFFDD24ED55D470E69E73AC50DE3FE5DA3ABE1EDF67F4C030A44DDF3FF5D73EA250C96BE3D327A84D963FE5DA32B91ED36BB1D132A31ED87AB1D021A255DF71B1C436BF479A7AF0C13AA14794"
ct = bytes.fromhex(s)#有很多不可打印的

# 遍历keylen和index的所有情况
for key_len in range(1, 30):
    for index in range(key_len):
        sub_arr = ct[index::key_len]  # 分组
        possible_ch = find_index_key(sub_arr)
        print('key_len = ', key_len, 'index = ', index, 'possible_ch = ', possible_ch)
        # 遍历所有可能的字符,解密ct中第一个长度为key_len的部分
        if possible_ch:
            k = []
            for j in possible_ch:
                k.append(chr(j ^ sub_arr[0]))
            print(k)

    # decryption
key = [186, 31, 145, 178, 83, 205, 62]
pt = ""
for i in range(len(ct)):
    pt += chr(ct[i] ^ key[i % 7])
print(pt)