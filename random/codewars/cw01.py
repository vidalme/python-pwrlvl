# ('Buy a !car [!red green !white] [cheap or !new]')  =>  ['Buy', 'a', '!car', '[!red green !white]', '[cheap or !new]']
# ('!Learning !javascript is [a joy]')                =>  ['!Learning', '!javascript', 'is', '[a joy]']
# ('[Cats and dogs] are !beautiful and [cute]')       =>  ['[Cats and dogs]', 'are', '!beautiful', 'and', '[cute]']

# '[srdutzjucj', 'Upoiqgzoyk', '!hgiesxqfh']         =>  ['srdutzjucj', 'Upoiqgzoyk', '!hgiesxqfh']

s1 = ('Buy a !car [!red green !white] [cheap or !new]')
s2 = ('!Learning !javascript is [a joy]')
s3 = ('[Cats and dogs] are !beautiful and [cute]')
s4 = ('[andre] [vidal [almeida')
s5 = ('Qbaaouhhuq Dgxvtbznpe [Ohykzfdrch !Sqypyqwgz] !fwttvdmxe [Vkdzepamsy] [!zhybrawyi Svazxcppkk Rkpllhciin] [Gowkgpaisy] [Ukvqkufrtx sforchpnxx !Bbnbwasiy')
s6 = ('Qbaaouhhuq Dgxvtbznpe [Ohykzfdrch !Sqypyqwgz] !fwttvdmxe [Vkdzepamsy] [!zhybrawyi Svazxcppkk Rkpllhciin] [Gowkgpaisy] Ukvqkufrtx sforchpnxx [!Bbnbwasiy')
s7 = ('['']')

def clever_split(s):
    if s == '['']':
        return []
    lista = s.split(" ")
    nova_lista=[]
    i = 0
    t = 0
    for word in lista:
        nova_word = word
        if word.startswith('['):
            nova_word = word.replace('[','')
            t=i
        if word.endswith(']'):
            temp_lista = []
            for j in range(t,i):nova_lista.pop(-1)
            for j in range(t,i+1):temp_lista.append(lista[j])
            nova_word = " ".join(temp_lista)
        nova_lista.append(nova_word)
        i+=1
    return nova_lista
    

print(clever_split(s7))


# perfect solution with lists
# def clever_split(s):
#     sa = s.split(" ")
#     print(sa)
#     acc=[]
#     ib = False
#     for sb in sa:
#         if sb.startswith('['): 
#             ib = True
#             acc.append(sb)
#         elif ib: acc[len(acc)-1]+=f" {sb}"
#         if sb.endswith(']'): ib = False
#         elif not ib: acc.append(sb)
#     return acc


# ['!Mrvlowizc', '!hbqqyyzby', '[!Hqnvjvdsi]', '[Dbpasrwmgz Eqqbseaafa mpizfeffah !Kxsbzjvpa !euolbapho]', 'ehxaqmjdti', '!gfytghbsu', 'uvyiocrmkk', '!ibonlrufp', '[!npszvknit]', '!Wcfxxlisy', '!Vonghdtrj', '[Zrlizpqnyr]', 'Frapzewcfx', '!Dstczdktl', 'Euxyxgzekr', 'juqvsitswz', 'Smjoutfgbn', '[!Sqpakihww !Wevvlllpy Oxmwdhgqqi]', '[Geyoawwcej nuxdcqzgjk]', 'Uwseponkxz', '[bcmxmqotdk !Tlkrpeqfg]', '[Lebmwwvweq Dfairavbbu jrlauqklpg]', 'tlshpmipry', 'paltauqeeg', '[Rhgwljjuuz !Amxihfijn !Vhyryhobi]', 'Jgtduwsewr', '[!hwfxdyiuz]', '[vjalzntmyt]', '!Tvzatktjv', '!bzxshkpjx', '[!Wsevvdumh !Onjdmvzgi !Mvbfohdoa !lpdcoimgi ursylviifk]', '!Gztgwriov', '!Hxewectji', '!tbbuezmht', 'ygjefqibad', '[!zpsikpaky]', 'Yxxvlgaqun', '[!Oyizdqxla]', '!Mwpnrgjqe', '[Iykbcuagwr irtwscxcsq Zbwnvrgagj]', '[!Lnksymthm xaqqhnwvvd]', '!jzhdhkfzp', '[!Jstwpmwst'] 
# ['!Mrvlowizc', '!hbqqyyzby', '[!Hqnvjvdsi]', '[Dbpasrwmgz Eqqbseaafa mpizfeffah !Kxsbzjvpa !euolbapho]', 'ehxaqmjdti', '!gfytghbsu', 'uvyiocrmkk', '!ibonlrufp', '[!npszvknit]', '!Wcfxxlisy', '!Vonghdtrj', '[Zrlizpqnyr]', 'Frapzewcfx', '!Dstczdktl', 'Euxyxgzekr', 'juqvsitswz', 'Smjoutfgbn', '[!Sqpakihww !Wevvlllpy Oxmwdhgqqi]', '[Geyoawwcej nuxdcqzgjk]', 'Uwseponkxz', '[bcmxmqotdk !Tlkrpeqfg]', '[Lebmwwvweq Dfairavbbu jrlauqklpg]', 'tlshpmipry', 'paltauqeeg', '[Rhgwljjuuz !Amxihfijn !Vhyryhobi]', 'Jgtduwsewr', '[!hwfxdyiuz]', '[vjalzntmyt]', '!Tvzatktjv', '!bzxshkpjx', '[!Wsevvdumh !Onjdmvzgi !Mvbfohdoa !lpdcoimgi ursylviifk]', '!Gztgwriov', '!Hxewectji', '!tbbuezmht', 'ygjefqibad', '[!zpsikpaky]', 'Yxxvlgaqun', '[!Oyizdqxla]', '!Mwpnrgjqe', '[Iykbcuagwr irtwscxcsq Zbwnvrgagj]', '[!Lnksymthm xaqqhnwvvd]', '!jzhdhkfzp', '!Jstwpmwst']