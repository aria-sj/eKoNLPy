# eKoNLPy - e(conomic)KoNLPy

eKoNLPy is a Python package for natural language processing (NLP) of the Korean language for economic analysis. 

KoNLPy의 Mecab tagger를 기반으로 경제관련 전문용어, 금융기관, 기업명 등을 하나의 명사로 분류하도록 후처리 기능을 추가.

통화정책(Monetary Policy)의 어조(Hawkish/Dovish)를 판단할 수 있는 Sentiment Analysis 기능 포함.

금융/경제분야에 적합한 감성사전 추가 예정.

Supervised learning에 기반한 금융/경제분야 Sentiment Analysis 기능도 추가 예정.


# Usage

## Part of speech tagging

KoNLPy와 동일하게 Mecab.pos(phrase)를 입력합니다.
먼저 KoNLPy의 Mecab 형태소 분석기로 처리한 후,
템플릿에 등록된 연속된 토큰의 조합이 사용자 사전에 등록되어 있으면
복합명사로 어절을 분리합니다.

    from ekonlpy.tag import Mecab
    mecab = Mecab()
    mecab.pos('금통위는 따라서 물가안정과 병행, 경기상황에 유의하는 금리정책을 펼쳐나가기로 했다고 밝혔다.')

    > [('금통위', 'NNG'), ('는', 'JX'), ('따라서', 'MAJ'), ('물가', 'NNG'), ('안정', 'NNG'), ('과', 'JC'), ('병행', 'NNG'), (',', 'SC'), ('경기', 'NNG'), ('상황', 'NNG'), ('에', 'JKB'), ('유의', 'NNG'), ('하', 'XSV'), ('는', 'ETM'), ('금리정책', 'NNG'), ('을', 'JKO'), ('펼쳐', 'VV+EC'), ('나가', 'VX'), ('기', 'ETN'), ('로', 'JKB'), ('했', 'VV+EP'), ('다고', 'EC'), ('밝혔', 'VV+EP'), ('다', 'EF'), ('.', 'SF')]

### Lemmatisation and synoyms

Sentiment 분석의 정확도를 높이기 위해, 동의어 처리와 lemmatization 기능을 제공한다.


### Add words to dictionary

ekonlpy.tag의 Mecab은 add_dictionary를 통하여 str 혹은 list of str 형식의 사용자 사전을 추가할 수 있습니다.

    from ekonlpy.tag import Mecab
    mecab = Mecab()
    mecab.add_dictionary('금통위', 'NNG')

## Sentiment analysis

To use the Korean Monetary Policy dictionary, create an instance of the `MPKO` class


    from ekonlpy.sentiment import MPKO
    mpko = MPKO(kind=1)
    tokens = mpko.tokenize(text)
    score = mpko.get_score(tokens)

`kind` parammeter for `MPKO` class: a parameter to select a lexicon file

    0: a lexicon file generated using Naive-bayes classifier with 5-gram tokens as features and
        changes of call rates as positive/negative label.

    1: a lexicon file generated by polarity induction and seed propagation method with 5-gram tokens.

    2: a lexicon file to measure uncertainty, which is generated by seed propagation method.

``KSA`` is a korean sentiment analyzer for general korean texts. 
KSA는 일반적인 한국어 감성분석 용도로 사용합니다. 형태소 분석기는 서울대학교 IDS 연구실에서 만든 꼬꼬마를 사용한다.
감성사전 또한 동 연구소의 것을 사용한다. (참고: http://kkma.snu.ac.kr/)

    from ekonlpy.sentiment import KSA
    ksa = KSA()
    tokens = ksa.tokenize(text)
    score = ksa.get_score(tokens)


Similarly, to use the Harvard IV-4 dictionary for general english sentiment analysis:


    from ekonlpy.sentiment import HIV4
    lm = HIV4()
    tokens = lm.tokenize(text)
    score = lm.get_score(tokens)

Similarly, to use the Loughran and McDonald dictionary for financial domain sentiment analysis:


    from ekonlpy.sentiment import LM
    lm = LM()
    tokens = lm.tokenize(text)
    score = lm.get_score(tokens)

## Install

    $ git clone https://github.com/entelecheia/eKoNLPy.git

    $ cd eKoNLPy

    $ pip install .

## Requires

- KoNLPy >= 0.4.4
