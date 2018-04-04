mecab_tags = {
    'NNG': '일반 명사',
    'NNP': '고유 명사',
    'NNB': '의존 명사',
    'NNBC': '단위를 나타내는 명사',
    'NR': '수사',
    'NP': '대명사',
    'VV': '동사',
    'VVX': '파생동사 (추가)',
    'VA': '형용사',
    'VAX': '파생형용사 (추가)',
    'VX': '보조 용언',
    'VCP': '긍정 지정사',
    'VCN': '부정 지정사',
    'MM': '관형사',
    'MAG': '일반 부사',
    'MAJ': '접속 부사',
    'IC': '감탄사',
    'JKS': '주격 조사',
    'JKC': '보격 조사',
    'JKG': '관형격 조사',
    'JKO': '목적격 조사',
    'JKB': '부사격 조사',
    'JKV': '호격 조사',
    'JKQ': '인용격 조사',
    'JC': '접속 조사',
    'JX': '보조사',
    'EP': '선어말어미',
    'EF': '종결 어미',
    'EC': '연결 어미',
    'ETN': '명사형 전성 어미',
    'ETM': '관형형 전성 어미',
    'XPN': '체언 접두사',
    'XSN': '명사파생 접미사',
    'XSV': '동사 파생 접미사',
    'XSA': '형용사 파생 접미사',
    'XR': '어근',
    'SF': '마침표, 물음표, 느낌표',
    'SE': '줄임표 …',
    'SSO': '여는 괄호 (, [',
    'SSC': '닫는 괄호 ), ]',
    'SC': '구분자 , · / :',
    'SY': '기타 기호',
    'SH': '한자',
    'SL': '외국어',
    'SN': '숫자'
}
# 'NNX': '파생 명사',
# SL: (?<=\n)[A-Za-z\s-\d]+\n
nouns_tags = ['NNG', 'NNP', 'UNKNOWN']
topic_tags = ['NNG']
stop_tags = ['SY', 'SF', 'SN', 'SH', 'SSO', 'SSC', 'SC', 'SE']
sent_tags = ['MAG', 'NNG', 'VV', 'VA', 'VVX', 'VAX', 'VX', 'VCN']
skip_tags = ['SC', 'SN', 'SY']

nochk_tags = {
    ('VX', 'NNG'): 'NNG',
    ('XPN', 'XR', 'XSN'): 'NNG'
}

xse_tags = {
    ('NNG', 'VCP'): 'VVX',
    ('NNG', 'XSA'): 'VAX',
    ('NNG', 'XSA+ETM'): 'VAX',
    ('NNG', 'XSV'): 'VVX',
    ('NNG', 'XSV+ETM'): 'VVX',
    ('NNG', 'XSV+EC'): 'VVX',
    ('NNG', 'XSV+EF'): 'VVX',
    ('NNG', 'XSV+EP'): 'VVX',
    ('NNG', 'XSV+EP+EC'): 'VVX',
    ('XR', 'XSA'): 'VAX',
    ('XR', 'XSA+ETM'): 'VAX',
    ('XR', 'XSV'): 'VVX'
}

xsn_sfx_tag = ('NNG', 'XSN')
suffix_tags = {
    'VA': ['적'],
    'NNG': ('감', '권', '계', '력', '률', '별', '분', '성', '용', '율', '자', '치', '화', '형'),
    'NNBC': ['당']
}
# 'NNX': ('상'),

skip_chk_tags = {
    ('MM', 'SC', 'NNG', 'SC', 'NR'): 'NNG',
    ('NNG', 'SC', 'NNG'): 'NNG',
    ('NNG', 'SY', 'NNG'): 'NNG',
    ('NNG', 'SY', 'NNG', 'XSN'): 'NNG',
    ('SN', 'NNBC', 'NNG'): 'NNG',
    ('SN', 'NNBC', 'VV'): 'NNG'
}

chk_tags = {
    ('IC', 'IC'): 'NNG',
    ('IC', 'NNG'): 'NNG',
    ('IC', 'NNG', 'NNG'): 'NNG',
    ('IC', 'NNG', 'NNG', 'NNG'): 'NNG',
    ('IC', 'NNG', 'NNG', 'NNG', 'NNG'): 'NNG',
    ('IC', 'VV', 'EC', 'NNG'): 'NNG',
    ('JKG', 'NNG'): 'NNG',
    ('JKS', 'NNG'): 'NNG',
    ('JKS', 'NNG', 'NNG'): 'NNG',
    ('JX', 'NNG'): 'NNG',
    ('MAG', 'MAG', 'VV'): 'NNG',
    ('MAG', 'NNG'): 'NNG',
    ('MAJ', 'MAG', 'IC'): 'NNG',
    ('MAJ', 'MAG', 'NNG'): 'NNG',
    ('MM', 'IC', 'NNG'): 'NNG',
    ('MM', 'IC', 'NNG', 'NNG'): 'NNG',
    ('MM', 'IC', 'NNG', 'NNG', 'NNG'): 'NNG',
    ('MM', 'NNG'): 'NNG',
    ('MM', 'NNG', 'NNG'): 'NNG',
    ('MM', 'NNG', 'NNG', 'NNG'): 'NNG',
    ('MM', 'NNG', 'NNG', 'NNG', 'NNG'): 'NNG',
    ('MM', 'NNG', 'XSN'): 'NNG',
    ('NNB', 'NNG'): 'NNG',
    ('NNB', 'NNG', 'JKS', 'NNG'): 'NNG',
    ('NNB+JX', 'NNG'): 'NNG',
    ('NNBC', 'MAG', 'VV'): 'NNG',
    ('NNBC', 'NNG'): 'NNG',
    ('NNG', 'IC', 'NNG'): 'NNG',
    ('NNG', 'JC'): 'NNG',
    ('NNG', 'JKB'): 'NNG',
    ('NNG', 'JKB', 'MM', 'NNG'): 'NNG',
    ('NNG', 'JKB', 'NNG'): 'NNG',
    ('NNG', 'JKB', 'VA', 'NNG'): 'NNG',
    ('NNG', 'JKB+JX', 'NNG'): 'NNG',
    ('NNG', 'JKG'): 'NNG',
    ('NNG', 'JKG', 'NNG'): 'NNG',
    ('NNG', 'JKO'): 'NNG',
    ('NNG', 'JKS'): 'NNG',
    ('NNG', 'JKS', 'NNG'): 'NNG',
    ('NNG', 'JKS', 'VV'): 'NNG',
    ('NNG', 'JX'): 'NNG',
    ('NNG', 'JX', 'NNG'): 'NNG',
    ('NNG', 'MAG'): 'NNG',
    ('NNG', 'MAG', 'NNG'): 'NNG',
    ('NNG', 'MAG', 'VV'): 'NNG',
    ('NNG', 'MAG', 'VV', 'NNG'): 'NNG',
    ('NNG', 'MAG', 'VV', 'VV'): 'NNG',
    ('NNG', 'MAG', 'VV+EC'): 'NNG',
    ('NNG', 'MAG', 'VV+EC', 'VV+ETM'): 'NNG',
    ('NNG', 'MAG', 'VV+ETM', 'NNG'): 'NNG',
    ('NNG', 'MM'): 'NNG',
    ('NNG', 'MM', 'NNG'): 'NNG',
    ('NNG', 'MM', 'NNG', 'NNG'): 'NNG',
    ('NNG', 'NNB'): 'NNG',
    ('NNG', 'NNB', 'NNG'): 'NNG',
    ('NNG', 'NNBC', 'NR', 'NNG'): 'NNG',
    ('NNG', 'NNG'): 'NNG',
    ('NNG', 'NNG', 'IC'): 'NNG',
    ('NNG', 'NNG', 'JC'): 'NNG',
    ('NNG', 'NNG', 'JKG'): 'NNG',
    ('NNG', 'NNG', 'JKS', 'NNG'): 'NNG',
    ('NNG', 'NNG', 'JX', 'MM'): 'NNG',
    ('NNG', 'NNG', 'JX', 'NNG'): 'NNG',
    ('NNG', 'NNG', 'MAG', 'NNG'): 'NNG',
    ('NNG', 'NNG', 'NNG'): 'NNG',
    ('NNG', 'NNG', 'NNG', 'JKS', 'NNG'): 'NNG',
    ('NNG', 'NNG', 'NNG', 'NNG'): 'NNG',
    ('NNG', 'NNG', 'NNG', 'NNG', 'NNG'): 'NNG',
    ('NNG', 'NNG', 'NNG', 'XSN'): 'NNG',
    ('NNG', 'NNG', 'NNG', 'XSN', 'NNG'): 'NNG',
    ('NNG', 'NNG', 'NNG', 'XSN', 'VV'): 'NNG',
    ('NNG', 'NNG', 'NR'): 'NNG',
    ('NNG', 'NNG', 'VA', 'IC'): 'NNG',
    ('NNG', 'NNG', 'VA', 'NNG'): 'NNG',
    ('NNG', 'NNG', 'VV', 'NNG'): 'NNG',
    ('NNG', 'NNG', 'XSN'): 'NNG',
    ('NNG', 'NNG+JX'): 'NNG',
    ('NNG', 'NNG+JX', 'MAG', 'NNG'): 'NNG',
    ('NNG', 'NP'): 'NNG',
    ('NNG', 'NR'): 'NNG',
    ('NNG', 'NR', 'NNG'): 'NNG',
    ('NNG', 'SL'): 'NNG',
    ('NNG', 'SL', 'NNG'): 'NNG',
    ('NNG', 'SL', 'SN'): 'NNG',
    ('NNG', 'SN', 'NNG'): 'NNG',
    ('NNG', 'SY', 'SN'): 'NNG',
    ('NNG', 'VCP', 'EC', 'NNG'): 'NNG',
    ('NNG', 'VCP', 'EC+VX+ETM', 'NNG'): 'NNG',
    ('NNG', 'VCP', 'NNG'): 'NNG',
    ('NNG', 'VCP', 'NNG', 'NNG'): 'NNG',
    ('NNG', 'VCP+EP', 'NNG'): 'NNG',
    ('NNG', 'VV'): 'NNG',
    ('NNG', 'VV', 'EC'): 'NNG',
    ('NNG', 'VV', 'NNB'): 'NNG',
    ('NNG', 'VV', 'NNG'): 'NNG',
    ('NNG', 'VV+EC', 'NNG'): 'NNG',
    ('NNG', 'VV+ETM', 'NNG'): 'NNG',
    ('NNG', 'VV+ETN'): 'NNG',
    ('NNG', 'XPN'): 'NNG',
    ('NNG', 'XSN'): 'NNG',
    ('NNG', 'XSN', 'JC'): 'NNG',
    ('NNG', 'XSN', 'JC', 'NNG'): 'NNG',
    ('NNG', 'XSN', 'JKB', 'MM', 'NNG'): 'NNG',
    ('NNG', 'XSN', 'JKB', 'NNG'): 'NNG',
    ('NNG', 'XSN', 'JKB+JX', 'NNG'): 'NNG',
    ('NNG', 'XSN', 'MM', 'NNG'): 'NNG',
    ('NNG', 'XSN', 'MM', 'NNG', 'NNG'): 'NNG',
    ('NNG', 'XSN', 'NNG'): 'NNG',
    ('NNG', 'XSN', 'NNG', 'NNG'): 'NNG',
    ('NNG', 'XSN', 'NNG', 'NNG', 'NNG'): 'NNG',
    ('NNG', 'XSV', 'MM', 'NNG'): 'NNG',
    ('NNG', 'XSV', 'MM', 'NNG', 'NNG'): 'NNG',
    ('NNG', 'XSV', 'NNG'): 'NNG',
    ('NNG', 'XSV', 'NNG', 'NNG'): 'NNG',
    ('NNG', 'XSV', 'NNG', 'NNG', 'NNG'): 'NNG',
    ('NNG', 'XSV+EC', 'MM', 'NNG'): 'NNG',
    ('NNG+JX', 'NP'): 'NNG',
    ('NP', 'IC', 'NNG'): 'NNG',
    ('NP', 'JKB', 'NNG'): 'NNG',
    ('NP', 'NNG'): 'NNG',
    ('NP', 'NNG', 'NNG'): 'NNG',
    ('NP', 'VV', 'NNG'): 'NNG',
    ('NP', 'VV+ETM', 'NNG'): 'NNG',
    ('NP+JKG', 'NNG'): 'NNG',
    ('NR', 'NNBC'): 'NNG',
    ('NR', 'NNBC', 'NNG'): 'NNG',
    ('NR', 'NNG'): 'NNG',
    ('NR', 'NNG', 'NNG'): 'NNG',
    ('NR', 'NNG', 'NNG', 'NNG'): 'NNG',
    ('SL', 'NNG'): 'NNG',
    ('SL', 'NNG', 'NNG'): 'NNG',
    ('SL', 'NNG', 'NNG', 'NNG'): 'NNG',
    ('SL', 'NNG', 'SL'): 'NNG',
    ('SL', 'SC', 'SL'): 'SL',
    ('SL', 'SN'): 'SL',
    ('SL', 'SN', 'NNG'): 'NNG',
    ('SL', 'SY', 'NNG'): 'NNG',
    ('SL', 'SY', 'SL'): 'SL',
    ('SN', 'NNBC', 'NNG'): 'NNG',
    ('SN', 'NNG'): 'NNG',
    ('SN', 'SY', 'NNG'): 'NNG',
    ('SSO', 'NNG', 'SSC'): 'NNG',
    ('VCP', 'EC', 'NNG'): 'NNG',
    ('VCP', 'EC', 'NNG', 'NNG'): 'NNG',
    ('VCP', 'NNG'): 'NNG',
    ('VV', 'EC'): 'NNG',
    ('VV', 'EC', 'NNG'): 'NNG',
    ('VV', 'EC', 'VX', 'NNG'): 'NNG',
    ('VV', 'EP'): 'NNG',
    ('VV', 'IC'): 'NNG',
    ('VV', 'IC', 'NNG'): 'NNG',
    ('VV', 'MAG'): 'NNG',
    ('VV', 'NNB'): 'NNG',
    ('VV', 'NNG'): 'NNG',
    ('VV', 'NNG', 'NNG'): 'NNG',
    ('VV', 'NP', 'NNG', 'NNG', 'NNG'): 'NNG',
    ('VV+EC', 'IC'): 'NNG',
    ('VV+EC', 'MAG'): 'NNG',
    ('VV+ETM', 'NNG'): 'NNG',
    ('VV+ETM', 'NNG', 'NNG'): 'NNG',
    ('VX', 'EC', 'NNG'): 'NNG',
    ('VX', 'NNG'): 'NNG',
    ('XPN', 'MAG'): 'NNG',
    ('XPN', 'NNG'): 'NNG',
    ('XPN', 'NNG', 'NNG'): 'NNG',
    ('XPN', 'XR'): 'NNG',
    ('XPN', 'XR', 'XSN'): 'NNG',
    ('XR', 'NNG'): 'NNG',
    ('XSN', 'NNG'): 'NNG'
}
