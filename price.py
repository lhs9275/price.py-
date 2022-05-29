def shopping(shop_file):
    k = "./data/"+shop_file+""
    def myWget(filename):
    # 다운로드 대상 파일 경로
        file_url = base_url + filename

    # 저장 경로와 파일명
        target_path = data_path / filename

        return urlretrieve(file_url, target_path)

    myWget(shop_file)

    shop_dict = {} # 생성할 사전 객체   

    with open(k,'r',encoding='utf-8') as f:
        lines = f.read()
        lines =lines.split("\n")
    for line in lines[2:]:
        if len(line)>0:
            name, price = line.strip().split()
        if price != '점수':
            shop_dict[name] = price

    return shop_dict



def item_price(shop_file, item):
    k = "./data/"+shop_file+""
    def myWget(filename):
    # 다운로드 대상 파일 경로
        file_url = base_url + filename

    # 저장 경로와 파일명
        target_path = data_path / filename

        return urlretrieve(file_url, target_path)

    myWget(shop_file)

    shop_dict = {} # 생성할 사전 객체   

    with open(k,'r',encoding='utf-8') as f:
        lines = f.read()
        lines =lines.split("\n")
    for line in lines[2:]:
        if len(line)>0:
            name, price = line.strip().split()
        if price != '점수':
            shop_dict[name] = price


    return(shop_dict[item])