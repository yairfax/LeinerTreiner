taamim={
    'ZAR2':'zarka',
    'SGL1':'SEGOL',
    'RVI2':'rivii',
    'MHP4':'mapakh',
    'PSH2':'pashta',
    'MER4':'mercha',
    'TIP1':'tipcha',
    'ATN0':'etnachta',
    'PAZ3':'pazer',
    'TLQ4':'tlisha-ktana',
    'TLG3':'tlisha-gdola',
    'QAD4':'kadma',
    'DAR4':'darga',
    'TVR2':'tvir',
    'YTV2':'yetiv',
    'SHA1':'shalshelet',
    'SLQ0':'sof-pasuk',
    'GRM3':'gershaim'
}

if notes(i)=='GER3':
    if i==0:
        out.append('azla-geresh')
    else:
        j=i-1
        while j>0 and notes[j]=='MUN4' or notes[j]=='MQF5':
            j-=1
        if notes[j]=='QAD4':
            out.append('vazla')
        else:
            out.append('azla-geresh')

if notes[i]=='MUN4':
    j=i
    while notes[j+1]=='MQF5':
        j+=1
    if notes[j+1]=='ZAR2':
        out.append('munach-zarka')
    elif notes[j+1]=='SGL1':
        out.append('munach-segol')
    elif notes[j+1]=='RVI2':
        out.append('munach-rvii')
    elif notes[j+1]=='ATN0':
        out.append('munach-etnachta')
    elif notes[j+1]=='MUN4':
        while notes[j+1]=='MUN4':
            while notes[j+1]=='MQF5':
                j+=1
            j+=1
        if notes[j+1]=='ZAR2':
            out.append('munach-zarka')
        elif notes[j+1]=='SGL1':
            out.append('munach-segol')
        elif notes[j+1]=='RVI2':
            out.append('munach-munach-rvii')
        elif notes[j+1]=='ATN0':
            out.append('munach-etnachta')
        else:
            out.append('munach')
    else:
        out.append('munach')
        
        

check munach
check azla/geresh
    
    
