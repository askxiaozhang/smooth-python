def name(chapter):
    print("-".join([i.lower() for i in chapter.split(" ")]))

def ChapterName(chapter):
    print("-".join(chapter.split(" ")))

if __name__ == "__main__":
    name("Incremental assignment of the sequence")
    name("List derivation and generator expressions")

    name("Use bisect to manage sorted sequences") # 用bisect来管理已排序的序列
    name("When the list is not preferred") #当列表不是首选时

    ChapterName("Dict and Set")# 字典和集合
    name("Generic mapping type") # 泛映射类型
    name("Dictionary derivation") # 字典推导