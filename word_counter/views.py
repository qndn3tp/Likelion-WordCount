from django.shortcuts import render

# ����� ��û�� ���� �� index.html ����
def index(request) :
    return render(request, 'index.html')

# word count�� �����ϴ� �ٽ� �κ�
def result(request) :
    sentence = str(request.POST.get("sentence"))
    sentence_to_list = sentence.split()
    
    dic = {}
    
    for word in sentence_to_list:
        if word in dic:
            dic[word] += 1
        else:
            dic[word] = 1
            
    # [(key1, value2), (key2, value2)] ���·� ����
    word_count = list(dic.items())
    
    # ��û�� ���� �� result.html, word_count ����
    return render(request, 'result.html', {'word_count':word_count})

