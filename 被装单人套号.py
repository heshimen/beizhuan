import os
#身高归档，使它符合165、170这种形式
def hi(sg1):
    while True:
        if sg1%5==1:
            return int(sg1)-1
        elif sg1%5==2:
            return sg1-2
        elif sg1%5==3:
            return sg1+2
        elif sg1%5==4:
            return sg1+1
        elif sg1%5==0:
            return sg1
            break
        
def jyrbx(sw4):
    '''男警用绒背心型号

                       '''
    if sg<=165:
        ht1=['165/100', '165/96', '165/92', '165/88', '165/84','160/100', '160/96', '160/92', '160/88', '160/84']
    elif sg==170:
        ht1=['170/104', '170/100', '170/96', '170/92', '170/88']
    elif sg==175:
        ht1=['175/108', '175/104', '175/100', '175/96', '175/92']
    elif sg==180:
        ht1=['180/112', '180/108', '180/104', '180/100', '180/96']
    elif sg==185 or sg==190:
        ht1=['185/116', '185/112', '185/108', '185/104', '185/100','190/116', '190/112', '190/108', '190/104', '190/100']
    else:
        ht1=[]  
    while True:
        if str(sg)+'/'+str(sw4) in ht1:
            return str(sg)+'/'+str(sw4)
        elif str(sg)+'/'+str(sw4+1) in ht1:
            return str(sg)+'/'+str(sw4+1)
        elif str(sg)+'/'+str(sw4+2) in ht1:
            return str(sg)+'/'+str(sw4+2)
        elif str(sg)+'/'+str(sw4-1) in ht1:
            return str(sg)+'/'+str(sw4-1)
        elif str(sg)+'/'+str(sw4-2) in ht1:
            return str(sg)+'/'+str(sw4-2)
        else:
            return '没这号型...'

def jyrbx2(sw4):
    '''女警用绒背心型号

                       '''
    if sg==155:
        ht1=['155/76','155/80','155/84','155/88','155/92',]
    elif sg==160:
        ht1=['160/80','160/84','160/88','160/92','160/96',]
    elif sg==165:
        ht1=['165/84','165/88','165/92','165/96','165/100',]
    elif sg==170:
        ht1=['170/88','170/92','170/96','170/100','170/104',]
    elif sg==175:
        ht1=['175/92','175/96','175/100','175/104','175/108',]
    else:
        ht1=[]  
    while True:
        if str(sg)+'/'+str(sw4) in ht1:
            return str(sg)+'/'+str(sw4)
        elif str(sg)+'/'+str(sw4+1) in ht1:
            return str(sg)+'/'+str(sw4+1)
        elif str(sg)+'/'+str(sw4+2) in ht1:
            return str(sg)+'/'+str(sw4+2)
        elif str(sg)+'/'+str(sw4-1) in ht1:
            return str(sg)+'/'+str(sw4-1)
        elif str(sg)+'/'+str(sw4-2) in ht1:
            return str(sg)+'/'+str(sw4-2)
        else:
            return '没这号型...'
            
def ktsy(sw):
    '''男宽体上衣型号

       通过身高、胸围判断'''
    if sg==160 or sg==165:
        kt1=['165/106', '165/100', '165/94', '165/88', '165/82']
    elif sg==170:
        kt1=['170/110', '170/104', '170/98', '170/92', '170/86']
    elif sg==175:
        kt1=['175/114', '175/108', '175/102', '175/96', '175/90']
    elif sg==180:
        kt1=['180/118', '180/112', '180/106', '180/100', '180/94']
    elif sg==185 or 190:
        kt1=['185/122', '185/116', '185/110', '185/104', '185/98']
    else:
        kt1=[] 
    while True:
        if str(sg)+'/'+str(sw) in kt1:
            return str(sg)+'/'+str(sw)
        elif str(sg)+'/'+str(sw-1) in kt1:
            return str(sg)+'/'+str(sw-1)
        elif str(sg)+'/'+str(sw-2) in kt1:
            return str(sg)+'/'+str(sw-2)
        elif str(sg)+'/'+str(sw+1) in kt1:
            return str(sg)+'/'+str(sw+1)
        elif str(sg)+'/'+str(sw+2) in kt1:
            return str(sg)+'/'+str(sw+2)
        elif str(sg)+'/'+str(sw+3) in kt1:
            return str(sg)+'/'+str(sw+3)
        else:
            return '没这号型...'

def ktxy(yw):
    '''男宽体下衣型号

       通过身高、胸围判断'''
    if sg==160 or sg==165:
        kt2=['165/98', '165/91', '165/84', '165/77', '165/70']
    elif sg==170:
        kt2=['170/102', '170/95', '170/88', '170/81', '170/74']
    elif sg==175:
        kt2=['175/106', '175/99', '175/92', '175/85', '175/78']
    elif sg==180:
        kt2=['180/110', '180/103', '180/96', '180/89', '180/82']
    elif sg==185 or 190:
        kt2=['185/114', '185/107', '185/100', '185/93', '185/86']
    else:
        kt1=[] 
    while True:
        if str(sg)+'/'+str(yw) in kt2:
            return str(sg)+'/'+str(yw)
        elif str(sg)+'/'+str(yw-1) in kt2:
            return str(sg)+'/'+str(yw-1)
        elif str(sg)+'/'+str(yw-2) in kt2:
            return str(sg)+'/'+str(yw-2)
        elif str(sg)+'/'+str(yw-3) in kt2:
            return str(sg)+'/'+str(yw-3)
        elif str(sg)+'/'+str(yw+1) in kt2:
            return str(sg)+'/'+str(yw+1)
        elif str(sg)+'/'+str(yw+2) in kt2:
            return str(sg)+'/'+str(yw+2)
        elif str(sg)+'/'+str(yw+3) in kt2:
            return str(sg)+'/'+str(yw+3)
        else:
            return '没这号型...'

def ktsy2(sw):
    '''女宽体上衣型号

       通过身高、胸围判断'''
    if sg==155:
        kt1=['155/78','155/84','155/90','155/96','155/102',]
    elif sg==160:
        kt1=['160/82','160/88','160/94','160/100','160/106',]
    elif sg==165:
        kt1=['165/86','165/92','165/98','165/104','165/110',]
    elif sg==170:
        kt1=['170/90','170/96','170/102','170/108','170/114',]
    elif sg==175:
        kt1=['175/94','175/100','175/106','175/112','175/118',]
    else:
        kt1=[] 
    while True:
        if str(sg)+'/'+str(sw) in kt1:
            return str(sg)+'/'+str(sw)
        elif str(sg)+'/'+str(sw-1) in kt1:
            return str(sg)+'/'+str(sw-1)
        elif str(sg)+'/'+str(sw-2) in kt1:
            return str(sg)+'/'+str(sw-2)
        elif str(sg)+'/'+str(sw+1) in kt1:
            return str(sg)+'/'+str(sw+1)
        elif str(sg)+'/'+str(sw+2) in kt1:
            return str(sg)+'/'+str(sw+2)
        elif str(sg)+'/'+str(sw+3) in kt1:
            return str(sg)+'/'+str(sw+3)
        else:
            return '没这号型...'

def ktxy2(yw):
    '''女宽体下衣型号

       通过身高、胸围判断'''
    if sg==155:
        kt2=['155/62','155/69','155/76','155/83','155/90',]
    elif sg==160:
        kt2=['160/66','160/73','160/80','160/87','160/94',]
    elif sg==165:
        kt2=['165/70','165/77','165/84','165/91','165/98',]
    elif sg==170:
        kt2=['170/74','170/81','170/88','170/95','170/102',]
    elif sg==175:
        kt2=['175/78','175/85','175/92','175/99','175/106',]
    else:
        kt2=[] 
    while True:
        if str(sg)+'/'+str(yw) in kt2:
            return str(sg)+'/'+str(yw)
        elif str(sg)+'/'+str(yw-1) in kt2:
            return str(sg)+'/'+str(yw-1)
        elif str(sg)+'/'+str(yw-2) in kt2:
            return str(sg)+'/'+str(yw-2)
        elif str(sg)+'/'+str(yw-3) in kt2:
            return str(sg)+'/'+str(yw-3)
        elif str(sg)+'/'+str(yw+1) in kt2:
            return str(sg)+'/'+str(yw+1)
        elif str(sg)+'/'+str(yw+2) in kt2:
            return str(sg)+'/'+str(yw+2)
        elif str(sg)+'/'+str(yw+3) in kt2:
            return str(sg)+'/'+str(yw+3)
        else:
            return '没这号型...'

def htsy2(sw):
    '''女合体上衣型号

       通过身高、胸围判断'''
    if hx=='A' and sg==150:
        ht1=['150/74A','150/78A','150/82A','150/86A','150/90A','150/94A',]
    elif hx=='A' and sg==155:
        ht1=['155/74A','155/78A','155/82A','155/86A','155/90A','155/94A','155/98A',]
    elif hx=='A' and sg==160:
        ht1=['160/74A','160/78A','160/82A','160/86A','160/90A','160/94A','160/98A','160/102A',]
    elif hx=='A' and sg==165:
        ht1=['165/74A','165/78A','165/82A','165/86A','165/90A','165/94A','165/98A','165/102A',]
    elif hx=='A' and sg==170:
        ht1=['170/78A','170/82A','170/86A','170/90A','170/94A','170/98A','170/102A',]
    elif hx=='A' and sg==175:
        ht1=['175/82A','175/86A','175/90A','175/94A','175/98A','175/102A',]
    elif hx=='A' and sg==180:
        ht1=['180/86A','180/90A','180/94A','180/98A','180/102A',]
    elif hx=='B' and sg==150:
        ht1=['150/76B','150/80B','150/84B','150/88B','150/92B','150/96B',]
    elif hx=='B' and sg==155:
        ht1=['155/76B','155/80B','155/84B','155/88B','155/92B','155/96B','155/100B',]
    elif hx=='B' and sg==160:
        ht1=['160/76B','160/80B','160/84B','160/88B','160/92B','160/96B','160/100B','160/104B',]
    elif hx=='B' and sg==165:
        ht1=['165/76B','165/80B','165/84B','165/88B','165/92B','165/96B','165/100B','165/104B','165/108B',]
    elif hx=='B' and sg==170:
        ht1=['170/76B','170/80B','170/84B','170/88B','170/92B','170/96B','170/100B','170/104B','170/108B',]
    elif hx=='B' and sg==175:
        ht1=['175/80B','175/84B','175/88B','175/92B','175/96B','175/100B','175/104B','175/108B',]
    elif hx=='B' and sg==180:
        ht1=['180/84B','180/88B','180/92B','180/96B','180/100B','180/104B','180/108B',]
    elif hx=='C' and sg==160:
        ht1=['160/80C','160/84C','160/88C','160/92C','160/96C','160/100C',]
    elif hx=='C' and sg==165:
        ht1=['165/80C','165/84C','165/88C','165/92C','165/96C','165/100C','165/104C',]
    elif hx=='C' and sg==170:
        ht1=['170/80C','170/84C','170/88C','170/92C','170/96C','170/100C','170/104C','170/108C',]
    elif hx=='C' and sg==175:
        ht1=['175/80C','175/84C','175/88C','175/92C','175/96C','175/100C','175/104C','175/108C','175/112C',]
    elif hx=='C' and sg==180:
        ht1=['180/84C','180/88C','180/92C','180/96C','180/100C','180/104C','180/108C','180/112C',]
    elif hx=='C' and sg==185:
        ht1=['185/88C','185/92C','185/96C','185/100C','185/104C','185/108C','185/112C',]
    elif hx=='C' and sg==190:
        ht1=['190/92C','190/96C','190/100C','190/104C','190/108C','190/112C',]
    else:
        ht1=[]  
    while True:
        if str(sg)+'/'+str(sw)+hx in ht1:
            return str(sg)+'/'+str(sw)+hx
        elif str(sg)+'/'+str(sw+1)+hx in ht1:
            return str(sg)+'/'+str(sw+1)+hx
        elif str(sg)+'/'+str(sw+2)+hx in ht1:
            return str(sg)+'/'+str(sw+2)+hx
        elif str(sg)+'/'+str(sw-1)+hx in ht1:
            return str(sg)+'/'+str(sw-1)+hx
        else:
            return '没这号型...'

def htxy2(yw):
    '''女合体下衣型号

       通过身高、胸围判断'''
    if hx=='A' and sg==150:
        ht2=['150/56A','150/58A','150/60A','150/62A','150/64A','150/66A','150/68A','150/70A','150/72A','150/74A','150/76A','150/78A','150/80A',]
    elif hx=='A' and sg==155:
        ht2=['155/56A','155/58A','155/60A','155/62A','155/64A','155/66A','155/68A','155/70A','155/72A','155/74A','155/76A','155/78A','155/80A','155/82A','155/84A',]
    elif hx=='A' and sg==160:
        ht2=['160/56A','160/58A','160/60A','160/62A','160/64A','160/66A','160/68A','160/70A','160/72A','160/74A','160/76A','160/78A','160/80A','160/82A','160/84A','160/86A','160/88A',]
    elif hx=='A' and sg==165:
        ht2=['165/56A','165/58A','165/60A','165/62A','165/64A','165/66A','165/68A','165/70A','165/72A','165/74A','165/76A','165/78A','165/80A','165/82A','165/84A','165/86A','165/88A',]
    elif hx=='A' and sg==170:
        ht2=['170/60A','170/62A','170/64A','170/66A','170/68A','170/70A','170/72A','170/74A','170/76A','170/78A','170/80A','170/82A','170/84A','170/86A','170/88A',]
    elif hx=='A' and sg==175:
        ht2=['175/64A','175/66A','175/68A','175/70A','175/72A','175/74A','175/76A','175/78A','175/80A','175/82A','175/84A','175/86A','175/88A',]
    elif hx=='A' and sg==180:
        ht2=['190/98A', '190/96A', '190/94A', '190/92A', '190/90A', '190/88A', '190/86A', '190/84A', '190/82A', '190/80A', '190/78A']
    elif hx=='B'and sg==150:
        ht2=['150/64B','150/66B','150/68B','150/70B','150/72B','150/74B','150/76B','150/78B','150/80B','150/82B','150/84B','150/86B',]
    elif hx=='B'and sg==155:
        ht2=['155/64B','155/66B','155/68B','155/70B','155/72B','155/74B','155/76B','155/78B','155/80B','155/82B','155/84B','155/86B','155/88B','155/90B',]
    elif hx=='B'and sg==160:
        ht2=['160/64B','160/66B','160/68B','160/70B','160/72B','160/74B','160/76B','160/78B','160/80B','160/82B','160/84B','160/86B','160/88B','160/90B','160/92B','160/94B',]
    elif hx=='B'and sg==165:
        ht2=['165/64B','165/66B','165/68B','165/70B','165/72B','165/74B','165/76B','165/78B','165/80B','165/82B','165/84B','165/86B','165/88B','165/90B','165/92B','165/94B','165/96B','165/98B',]
    elif hx=='B'and sg==170:
        ht2=['170/64B','170/66B','170/68B','170/70B','170/72B','170/74B','170/76B','170/78B','170/80B','170/82B','170/84B','170/86B','170/88B','170/90B','170/92B','170/94B','170/96B','170/98B',]
    elif hx=='B'and sg==175:
        ht2=['175/68B','175/70B','175/72B','175/74B','175/76B','175/78B','175/80B','175/82B','175/84B','175/86B','175/88B','175/90B','175/92B','175/94B','175/96B','175/98B',]
    elif hx=='B'and sg==180:
        ht2=['180/72B','180/74B','180/76B','180/78B','180/80B','180/82B','180/84B','180/86B','180/88B','180/90B','180/92B','180/94B','180/96B','180/98B',]
    elif hx=='C'and sg==160:
        ht2=['160/72C','160/74C','160/76C','160/78C','160/80C','160/82C','160/84C','160/86C','160/88C','160/90C','160/92C','160/94C',]
    elif hx=='C'and sg==165:
        ht2=['165/72C','165/74C','165/76C','165/78C','165/80C','165/82C','165/84C','165/86C','165/88C','165/90C','165/92C','165/94C','165/96C','165/98C',]
    elif hx=='C'and sg==170:
        ht2=['170/72C','170/74C','170/76C','170/78C','170/80C','170/82C','170/84C','170/86C','170/88C','170/90C','170/92C','170/94C','170/96C','170/98C','170/100C','170/102C','170/104C','170/106C', ]
    elif hx=='C'and sg==175:
        ht2=['175/72C','175/74C','175/76C','175/78C','175/80C','175/82C','175/84C','175/86C','175/88C','175/90C','175/92C','175/94C','175/96C','175/98C','175/100C','175/102C','175/104C','175/106C',]
    elif hx=='C'and sg==180:
        ht2=['180/76C','180/78C','180/80C','180/82C','180/84C','180/86C','180/88C','180/90C','180/92C','180/94C','180/96C','180/98C','180/100C','180/102C','180/104C','180/106C',]
    elif hx=='C'and sg==185:
        ht2=['185/80C','185/82C','185/84C','185/86C','185/88C','185/90C','185/92C','185/94C','185/96C','185/98C','185/100C','185/102C','185/104C','185/106C',]
    elif hx=='C'and sg==190:
        ht2=['190/84C','190/86C','190/88C','190/90C','190/92C','190/94C','190/96C','190/98C','190/100C','190/102C','190/104C','190/106C',]
    else:
        ht2=[]
    while True:
        if str(sg)+'/'+str(yw)+hx in ht2:
            return str(sg)+'/'+str(yw)+hx
        elif str(sg)+'/'+str(yw+1)+hx in ht2:
            return str(sg)+'/'+str(yw+1)+hx
        elif str(sg)+'/'+str(yw-1)+hx in ht2:
            return str(sg)+'/'+str(yw-1)+hx
        elif str(sg)+'/'+str(yw+2)+hx in ht2:
            return str(sg)+'/'+str(yw+2)+hx
        else:
            return '没这号型...'

def htsy(sw):
    '''男合体上衣型号

       通过身高、胸围判断'''
    if hx=='A' and sg==160:
        ht1=['160/94A', '160/90A', '160/86A', '160/82A', '160/78A']
    elif hx=='A' and sg==165:
        ht1=['165/98A', '165/94A', '165/90A', '165/86A', '165/82A', '165/78A']
    elif hx=='A' and sg==170:
        ht1=['170/102A', '170/98A', '170/94A', '170/90A', '170/86A', '170/82A', '170/78A']
    elif hx=='A' and sg==175:
        ht1=['175/110A', '175/106A', '175/102A', '175/98A', '175/94A', '175/90A', '175/86A', '175/82A']
    elif hx=='A' and sg==180:
        ht1=['180/110A', '180/106A', '180/102A', '180/98A', '180/94A', '180/90A', '180/86A']
    elif hx=='A' and sg==185:
        ht1=['185/110A', '185/106A', '185/102A', '185/98A', '185/94A', '185/90A']
    elif hx=='A' and sg==190:
        ht1=['190/110A', '190/106A', '190/102A', '190/98A', '190/94A']
    elif hx=='B' and sg==160:
        ht1=['160/104B', '160/100B', '160/96B', '160/92B', '160/88B', '160/84B']
    elif hx=='B' and sg==165:
        ht1=['165/108B', '165/104B', '165/100B', '165/96B', '165/92B', '165/88B', '165/84B']
    elif hx=='B' and sg==170:
        ht1=['170/112B', '170/108B', '170/104B', '170/100B', '170/96B', '170/92B', '170/88B', '170/84B']
    elif hx=='B' and sg==175:
        ht1=['175/116B', '175/112B', '175/108B', '175/104B', '175/100B', '175/96B', '175/92B', '175/88B', '175/84B']
    elif hx=='B' and sg==180:
        ht1=['180/116B', '180/112B', '180/108B', '180/104B', '180/100B', '180/96B', '180/92B', '180/88B']
    elif hx=='B' and sg==185:
        ht1=['185/116B', '185/112B', '185/108B', '185/104B', '185/100B', '185/96B', '185/92B']
    elif hx=='B' and sg==190:
        ht1=['190/116B', '190/112B', '190/108B', '190/104B', '190/100B', '190/96B']
    elif hx=='C' and sg==160:
        ht1=['160/108C', '160/104C', '160/100C', '160/96C', '160/92C', '160/88C']
    elif hx=='C' and sg==165:
        ht1=['165/112C', '165/108C', '165/104C', '165/100C', '165/96C', '165/92C', '165/88C']
    elif hx=='C' and sg==170:
        ht1=['170/116C', '170/112C', '170/108C', '170/104C', '170/100C', '170/96C', '170/92C', '170/88C']
    elif hx=='C' and sg==175:
        ht1=['175/120C', '175/116C', '175/112C', '175/108C', '175/104C', '175/100C', '175/96C', '175/92C', '175/88C']
    elif hx=='C' and sg==180:
        ht1=['180/120C', '180/116C', '180/112C', '180/108C', '180/104C', '180/100C', '180/96C', '180/92C']
    elif hx=='C' and sg==185:
        ht1=['185/120C', '185/116C', '185/112C', '185/108C', '185/104C', '185/100C', '185/96C']
    elif hx=='C' and sg==190:
        ht1=['190/120C', '190/116C', '190/112C', '190/108C', '190/104C', '190/100C']
    else:
        ht1=[]  
    while True:
        if str(sg)+'/'+str(sw)+hx in ht1:
            return str(sg)+'/'+str(sw)+hx
        elif str(sg)+'/'+str(sw+1)+hx in ht1:
            return str(sg)+'/'+str(sw+1)+hx
        elif str(sg)+'/'+str(sw+2)+hx in ht1:
            return str(sg)+'/'+str(sw+2)+hx
        elif str(sg)+'/'+str(sw-1)+hx in ht1:
            return str(sg)+'/'+str(sw-1)+hx
        else:
            return '没这号型...'

def htxy(yw):
    '''男合体下衣型号

       通过身高、胸围判断'''
    if hx=='A' and sg==160:
        ht2=['160/82A', '160/80A', '160/78A', '160/76A', '160/74A', '160/72A', '160/70A', '160/68A', '160/66A', '160/64A', '160/62A']
    elif hx=='A' and sg==165:
        ht2=['165/86A', '165/84A', '165/82A', '165/80A', '165/78A', '165/76A', '165/74A', '165/72A', '165/70A', '165/68A', '165/66A', '165/64A', '165/62A']
    elif hx=='A' and sg==170:
        ht2=['170/90A', '170/88A', '170/86A', '170/84A', '170/82A', '170/80A', '170/78A', '170/76A', '170/74A', '170/72A', '170/70A', '170/68A', '170/66A', '170/64A', '170/62A']
    elif hx=='A' and sg==175:
        ht2=['175/98A', '175/96A', '175/94A', '175/92A', '175/90A', '175/88A', '175/86A', '175/84A', '175/82A', '175/80A', '175/78A', '175/76A', '175/74A', '175/72A', '175/70A', '175/68A', '175/66A']
    elif hx=='A' and sg==180:
        ht2=['180/98A', '180/96A', '180/94A', '180/92A', '180/90A', '180/88A', '180/86A', '180/84A', '180/82A', '180/80A', '180/78A', '180/76A', '180/74A', '180/72A', '180/70A']
    elif hx=='A' and sg==185:
        ht2=['185/98A', '185/96A', '185/94A', '185/92A', '185/90A', '185/88A', '185/86A', '185/84A', '185/82A', '185/80A', '185/78A', '185/76A', '185/74A']
    elif hx=='A' and sg==190:
        ht2=['190/98A', '190/96A', '190/94A', '190/92A', '190/90A', '190/88A', '190/86A', '190/84A', '190/82A', '190/80A', '190/78A']
    elif hx=='B'and sg==160:
        ht2=['160/96B', '160/94B', '160/92B', '160/90B', '160/88B', '160/86B', '160/84B', '160/82B', '160/80B', '160/78B', '160/76B', '160/74B']
    elif hx=='B'and sg==165:
        ht2=['165/100B', '165/98B', '165/96B', '165/94B', '165/92B', '165/90B', '165/88B', '165/86B', '165/84B', '165/82B', '165/80B', '165/78B', '165/76B', '165/74B']
    elif hx=='B'and sg==170:
        ht2=['170/104B', '170/102B', '170/100B', '170/98B', '170/96B', '170/94B', '170/92B', '170/90B', '170/88B', '170/86B', '170/84B', '170/82B', '170/80B', '170/78B', '170/76B', '170/74B']
    elif hx=='B'and sg==175:
        ht2=['175/108B', '175/106B', '175/104B', '175/102B', '175/100B', '175/98B', '175/96B', '175/94B', '175/92B', '175/90B', '175/88B', '175/86B', '175/84B', '175/82B', '175/80B', '175/78B', '175/76B', '175/74B']
    elif hx=='B'and sg==180:
        ht2=['180/108B', '180/106B', '180/104B', '180/102B', '180/100B', '180/98B', '180/96B', '180/94B', '180/92B', '180/90B', '180/88B', '180/86B', '180/84B', '180/82B', '180/80B', '180/78B']
    elif hx=='B'and sg==185:
        ht2=['185/108B', '185/106B', '185/104B', '185/102B', '185/100B', '185/98B', '185/96B', '185/94B', '185/92B', '185/90B', '185/88B', '185/86B', '185/84B', '185/82B']
    elif hx=='B'and sg==190:
        ht2=['190/108B', '190/106B', '190/104B', '190/102B', '190/100B', '190/98B', '190/96B', '190/94B', '190/92B', '190/90B', '190/88B', '190/86B']
    elif hx=='C'and sg==160:
        ht2=['160/104C', '160/102C', '160/100C', '160/98C', '160/96C', '160/94C', '160/92C', '160/90C', '160/88C', '160/86C', '160/84C', '160/82C']
    elif hx=='C'and sg==165:
        ht2=['165/108C', '165/106C', '165/104C', '165/102C', '165/100C', '165/98C', '165/96C', '165/94C', '165/92C', '165/90C', '165/88C', '165/86C', '165/84C', '165/82C']
    elif hx=='C'and sg==170:
        ht2=['170/112C', '170/110C', '170/108C', '170/106C', '170/104C', '170/102C', '170/100C', '170/98C', '170/96C', '170/94C', '170/92C', '170/90C', '170/88C', '170/86C', '170/84C', '170/82C']
    elif hx=='C'and sg==175:
        ht2=['175/116C', '175/114C', '175/112C', '175/110C', '175/108C', '175/106C', '175/104C', '175/102C', '175/100C', '175/98C', '175/96C', '175/94C', '175/92C', '175/90C', '175/88C', '175/86C', '175/84C', '175/82C']
    elif hx=='C'and sg==180:
        ht2=['180/116C', '180/114C', '180/112C', '180/110C', '180/108C', '180/106C', '180/104C', '180/102C', '180/100C', '180/98C', '180/96C', '180/94C', '180/92C', '180/90C', '180/88C', '180/86C']
    elif hx=='C'and sg==185:
        ht2=['185/116C', '185/114C', '185/112C', '185/110C', '185/108C', '185/106C', '185/104C', '185/102C', '185/100C', '185/98C', '185/96C', '185/94C', '185/92C', '185/90C']
    elif hx=='C'and sg==190:
        ht2=['190/116C', '190/114C', '190/112C', '190/110C', '190/108C', '190/106C', '190/104C', '190/102C', '190/100C', '190/98C', '190/96C', '190/94C']
    else:
        ht2=[]
    while True:
        if str(sg)+'/'+str(yw)+hx in ht2:
            return str(sg)+'/'+str(yw)+hx
        elif str(sg)+'/'+str(yw+1)+hx in ht2:
            return str(sg)+'/'+str(yw+1)+hx
        elif str(sg)+'/'+str(yw-1)+hx in ht2:
            return str(sg)+'/'+str(yw-1)+hx
        elif str(sg)+'/'+str(yw+2)+hx in ht2:
            return str(sg)+'/'+str(yw+2)+hx
        else:
            return '没这号型...'



#套号：毛衣等特殊号型--下衣(男女相同)
#175、180、185都用175号型
def tshx(yw1):
    if sg==155:
        ht1=['155/83', '155/76', '155/69', '155/62']
    elif sg==160:
        ht1=['160/87', '160/80', '160/73', '160/66', '160/59']
    elif sg==165:
        ht1=['165/91', '165/84', '165/77', '165/70', '165/63']
    elif sg==170:
        ht1=['170/88', '170/81', '170/74', '170/67']
    elif sg>=175:
        ht1=['175/92', '175/85', '175/78', '175/71','180/92', '180/85', '180/78', '180/71','185/92', '185/85', '185/78', '185/71','190/92', '190/85', '190/78', '190/71'] #最大尺寸只到175
    else:
        ht1=[]  
    while True:
        if str(sg)+'/'+str(yw1) in ht1:
            return str(sg)+'/'+str(yw1)
        elif str(sg)+'/'+str(yw1+1) in ht1:
            return str(sg)+'/'+str(yw1+1)
        elif str(sg)+'/'+str(yw1+2) in ht1:
            return str(sg)+'/'+str(yw1+2)
        elif str(sg)+'/'+str(yw1+3) in ht1:
            return str(sg)+'/'+str(yw1+3)
        elif str(sg)+'/'+str(yw1-1) in ht1:
            return str(sg)+'/'+str(yw1-1)
        elif str(sg)+'/'+str(yw1-2) in ht1:
            return str(sg)+'/'+str(yw1-2)
        elif str(sg)+'/'+str(yw1-3) in ht1:
            return str(sg)+'/'+str(yw1-3)
        elif str(sg)+'/'+str(yw1+4) in ht1:
            return str(sg)+'/'+str(yw1+4)
        else:
            return '没这号型...'

#套号：毛衣等特殊号型--上衣(男女相同)
#175、180、185都用175号型
def tshx(sw1):
    if sg==155:
        ts1=['155/96', '155/90', '155/84', '155/78']
    elif sg==160:
        ts1=['160/100', '160/94', '160/88', '160/82', '160/76']
    elif sg==165:
        ts1=['165/104', '165/98', '165/92', '165/86', '165/80']
    elif sg==170:
        ts1=['170/102', '170/96', '170/90', '170/84']
    elif sg==175:
        ts1=['175/106', '175/100', '175/94', '175/88'] #最大尺寸只到175
    else:
        print ('T,180,185,190没有对应号型，用175尝试')  
    while True:
        if str(sg)+'/'+str(sw1) in ts1:
            return str(sg)+'/'+str(sw1)
        elif str(sg)+'/'+str(sw1+1) in ts1:
            return str(sg)+'/'+str(sw1+1)
        elif str(sg)+'/'+str(sw1+2) in ts1:
            return str(sg)+'/'+str(sw1+2)
        elif str(sg)+'/'+str(sw1+3) in ts1:
            return str(sg)+'/'+str(sw1+3)
        elif str(sg)+'/'+str(sw1-1) in ts1:
            return str(sg)+'/'+str(sw1-1)
        elif str(sg)+'/'+str(sw1-2) in ts1:
            return str(sg)+'/'+str(sw1-2)
        elif str(sg)+'/'+str(sw1-3) in ts1:
            return str(sg)+'/'+str(sw1-3)
        else:
            return '没这号型...'+str(sg)+'/'+str(sw1+1)

#通过身高判断领带号型
def ld(ld):
    if ld<161:
        return '4'
    elif ld<171:
        return '3'
    elif ld<181:
        return '2'
    else:
        return '1'

#通过胸围判断内腰带
def nyd(yw):
    if yw<76:
        return '4号900'
    elif yw<86:
        return '3号1000'
    elif yw<96:
        return '2号1100'
    else:
        return '1号1200'

#通过胸围判断外腰带号型
def wyd(yw):
    if yw<78:
        return '1150'
    elif yw<90:
        return '1250'
    else:
        return '1350'

#通过头围判断头盔/面具号型
def tk(tw):
    if tw<56.4:
        return '小号（S）'
    elif tw<58.4:
        return '中号（M）'
    else:
        return '大号（L）'

def dk(yw):
    '''男短裤型号

       通过身高、胸围判断'''
    if yw<77:
        return '74'
    elif yw<83:
        return '80'
    elif yw<89:
        return '86'
    elif yw<95:
        return '92'
    elif yw<101:
        return '98'
    else:
        return '104'

def dk2(yw):
    '''女短裤型号

       通过身高、胸围判断'''
    if yw<67:
        return '64'
    elif yw<73:
        return '70'
    elif yw<79:
        return '76'
    elif yw<85:
        return '82'
    elif yw<91:
        return '88'
    else:
        return '104'

#鞋号，如果是40、41码的，转换为250、255的形式
def xz(xh):
    if xh<50:
        return (xh+10)*5
    else:
        return xh
    
        
xb=input('请输入性别（男：m,女：f,不区分大小写）')
sg=int(input('身高'))
ldhx=sg     #将身高赋予领带的参数备用
sg=hi(sg)    #调用函数，将身高归档
sw=int(input('胸围'))
yw=int(input('腰围'))
xh=int(input('鞋号'))
tw=int(input('头围'))
jw=int(input('颈围'))

if xb=='M' or xb=='m':
    if abs(sw-yw)>11:
        hx='A'
    elif abs(sw-yw)>6:
        hx='B'
    else:
        hx='C'

    print ('\n'+'合体上身型号:'+str(htsy(sw)))
    print ('合体下身型号:'+str(htxy(yw)))
    print ('衬衣型号:'+str(htsy(sw))+'/'+str(jw+2)+'\n')

    print ('宽体上身型号:'+str(ktsy(sw)))
    print ('宽体下身型号:'+str(ktxy(yw))+'\n')

    print ('警用绒背心:'+str(jyrbx(sw)))
    print ('特警短裤的型号：'+str(dk(yw))+'\n')

    print ('帽子的型号:'+str(tk(tw)))
    print ('头盔/面具的型号：'+str(tk(tw)))
    print ('鞋号:'+str(xz(xh))+'\n')

    print ('领带号型：'+str(ld(ldhx)))
    print ('内腰带号型：'+str(nyd(yw))) 
    print ('外腰带号型：'+str(wyd(yw)))


    print ('腰围点高:'+str(int(0.6*ldhx)))
elif xb=='F'or xb=='f':
    if abs(sw-yw)>13:
        hx='A'
    elif abs(sw-yw)>8:
        hx='B'
    else:
        hx='C'

    print ('\n'+'合体上身型号:'+str(htsy2(sw)))
    print ('合体下身型号:'+str(htxy2(yw)))
    print ('衬衣型号:'+str(htsy2(sw))+'/'+str(jw+2)+'\n')

    print ('宽体上身型号:'+str(ktsy2(sw)))
    print ('宽体下身型号:'+str(ktxy2(yw))+'\n')

    print ('警用绒背心:'+str(jyrbx2(sw)))
    print ('特警短裤的型号：'+str(dk2(yw))+'\n')

    print ('帽子的型号:'+str(tk(tw)))
    print ('头盔/面具的型号：'+str(tk(tw)))
    print ('鞋号:'+str(xz(xh))+'\n')

    print ('领带号型：'+str(ld(ldhx)))
    print ('内腰带号型：'+str(nyd(yw))) 
    print ('外腰带号型：'+str(wyd(yw)))

else:
    print ('性别输入错误')


    


ldy=' \n\n'+'性别:'+str(xb)+'    '+'身高:'+str(ldhx)+'    '+'胸围:'+str(sw)+'    '\
     +'腰围:'+str(yw)+'    '+'鞋号:'+str(xh)+'    '+'头围:'+str(tw)+'    '+'颈围:'+str(jw)+'\n'\
     +'合体上身型号:'+str(htsy(sw))+';\n'\
     +'合体下身型号:'+str(htxy(yw))+';\n'\
     +'衬衣型号:'+str(htsy(sw))+'/'+str(jw+2)+';\n\n'\
     +'宽体上身型号:'+str(ktsy(sw))+';\n'\
     +'宽体下身型号:'+str(ktxy(yw))+';\n\n'\
     +'警用绒背心:'+str(jyrbx(sw))+';\n'\
     +'特警短裤的型号：'+str(dk(yw))+';\n\n'\
     +'鞋号:'+str(xz(xh))+';\n'\
     +'内腰带号型：'+str(nyd(yw))+';\n'\
     +'外腰带号型'+str(wyd(yw))+';\n'\
     +'领带号型：'+str(ld(ldhx))+';\n'\
     +'头盔/面具的型号：'+str(tk(tw))+';\n'\
     +'腰围点高    :'+str(int(0.6*ldhx))


out=open('D:\\1.txt','a')
out.write(ldy)
out.close()



print ('\n'+'         版本1.0，制造DyyXn时间2017.7.21')
print ("data saves d:\\1.txt")
#特殊体型不用，暂时搁置    

    
