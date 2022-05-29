def shopping(shop_file):
    k = "./data/"+shop_file+""
    
    shop_dict = {} # 생성할 사전 객체   

    with open(k,'r',encoding='utf-8') as f:
        lines = f.read()
        lines =lines.split("\n")
        print(lines)
    for line in lines[2:]:
        if len(line)>0:
            name, num = line.strip().split()
        if num != '점수':
            shop_dict[name] = num

    return shop_dict



def item_price(shop_file, item):
    k = "./data/"+shop_file+""

    shop_dict = {} # 생성할 사전 객체   

    with open(k,'r',encoding='utf-8') as f:
        lines = f.read()
        lines =lines.split("\n")
    for line in lines[2:]:
        if len(line)>0:
            name, num = line.strip().split()
        if num != '점수':
            shop_dict[name] = num


    return(shop_dict[item])
