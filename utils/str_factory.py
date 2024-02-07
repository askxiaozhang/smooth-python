def name(chapter):
    print("-".join([i.lower() for i in chapter.split(" ")]))

if __name__ == "__main__":
    name("Incremental assignment of the sequence")
    name("List derivation and generator expressions")

    name("Use bisect to manage sorted sequences") # 用bisect来管理已排序的序列
    name("When the list is not preferred") #当列表不是首选时