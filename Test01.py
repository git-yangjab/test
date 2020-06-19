# -*- encoding: utf-8 -*-
'''
@File    :   Test01.py
@Time    :   2020/05/25 11:25:01
@Author  :   Daye
@Version :   1.0
@Desc    :   None
'''
import hanlp

def twoSum(nums, target: int):
        for i, n in enumerate(nums):
            m = target - n
            if m in nums[i+1:]:
                return i, nums[i+1:].index(m)+i+1

if __name__ == "__main__":
    tokenizer = hanlp.load('PKU_NAME_MERGED_SIX_MONTHS_CONVSEG')
    ciList = tokenizer('商品和服务')
    tagger = hanlp.load(hanlp.pretrained.pos.CTB5_POS_RNN_FASTTEXT_ZH)
    print(tagger(ciList))
    # print(tokenizer('商品和服务'))
    print(hanlp.pretrained.ALL)