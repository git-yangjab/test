# -*- encoding: utf-8 -*-
'''
@File    :   test1.py
@Time    :   2020/06/08 18:15:00
@Author  :   Daye
@Version :   1.0
@Desc    :   None
'''

# here put the import lib
import jieba
import jieba.analyse
  
def words2vec(words1=None, words2=None):
    v1 = []
    v2 = []
    tag1 = jieba.analyse.extract_tags(words1, withWeight=True)
    tag2 = jieba.analyse.extract_tags(words2, withWeight=True)
    tag_dict1 = {i[0]: i[1] for i in tag1}
    tag_dict2 = {i[0]: i[1] for i in tag2}
    merged_tag = set(tag_dict1.keys()) | set(tag_dict2.keys())
    for i in merged_tag:
        if i in tag_dict1:
            v1.append(tag_dict1[i])
        else:
            v1.append(0)
        if i in tag_dict2:
            v2.append(tag_dict2[i])
        else:
            v2.append(0)
    return v1, v2
  
  
def cosine_similarity(vector1, vector2):
    dot_product = 0.0
    normA = 0.0
    normB = 0.0
    for a, b in zip(vector1, vector2):
        dot_product += a * b
        normA += a ** 2
        normB += b ** 2
    if normA == 0.0 or normB == 0.0:
        return 0
    else:
        return round(dot_product / ((normA**0.5)*(normB**0.5)) * 100, 2)
      
def cosine(str1, str2):
    vec1, vec2 = words2vec(str1, str2)
    return cosine_similarity(vec1, vec2)
  
# print(cosine('天气预报说，明天会下雨，你明天早上去上班的时候记得带上伞。', '你明天早上去上班的时候记得带上伞，天气预报说的可能会下雨。'))

str1 = "点击☞桂林人别屯口罩了，多想想眼镜吧！十字街这家店刚开业就下血本送送送送！有话好好说，不要一言不合就脱裤子！据网友爆料，今天（4月6日）他从解放桥上经过时，突然发现一个大妈在解放桥下六匹马附近的草地里弯着腰，看样子是在摘野菜。这本来没什么好奇怪的，然而仔细一看，这位大妈下身竟然近乎裸露，只穿着一条几乎遮不住屁股的小短裤！只见这位大妈翘着臀部对着大桥，白花花的大腿完全暴露在空气中。桥上的行人都露出不可思议的表情，有带着小孩的更是在桥上指责起来。不过也有网友猜测，该大妈可能是游泳上来后去摘菜的。据目击网友透露，目测该大妈年纪在50岁左右。小编寻思着这天气也没有很热呀，如此做派在公共场合不仅不雅，而且也容易着凉呀！不管是不是刚游了泳上岸，还是赶紧把裤子穿上吧！加客服带你进天天看粉丝群来源：桂林人论坛桂林天天看综合编辑（版权归原作者）合作联系微信：zl123cn   点击☞桂林人别屯口罩了，多想想眼镜吧！十字街这家店刚开业就下血本送送送送！"
str2 = "点击☞桂林人别屯口罩了，多想想眼镜吧！十字街这家店刚开业就下血本送送送送！有话好好说，不要一言不合就脱裤子！据网友爆料，今天（4月6日）他从解放桥上经过时，突然发现一个大妈在解放桥下六匹马附近的草地里弯着腰，看样子是在摘野菜。这本来没什么好奇怪的，然而仔细一看，这位大妈下身竟然近乎裸露，只穿着一条几乎遮不住屁股的小短裤！只见这位大妈翘着臀部对着大桥，白花花的大腿完全暴露在空气中。桥上的行人都露出不可思议的表情，有带着小孩的更是在桥上指责起来。不过也有网友猜测，该大妈可能是游泳上来后去摘菜的。据目击网友透露，目测该大妈年纪在50岁左右。小编寻思着这天气也没有很热呀，如此做派在公共场合不仅不雅，而且也容易着凉呀！不管是不是刚游了泳上岸，还是赶紧把裤子穿上吧！加客服带你进天天看粉丝群来源：桂林人论坛桂林天天看综合编辑（版权归原作者）合作联系微信：zl123cn   点击☞桂林人别屯口罩了，多想想眼镜吧！十字街这家店刚开业就下血本送送送送！"
print(cosine(str1,str2))