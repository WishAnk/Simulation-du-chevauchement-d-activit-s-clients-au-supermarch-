

import matplotlib.pyplot as plt
import numpy as np 




def alea(IX, IY,IZ):
    IX[0] = 171 * (IX[0]%177) - 2 * (IX[0] // 177) 
    IY[0] = 172 * (IY[0] % 176) -35*(IY[0] // 176)
    IZ[0]  = 170 * (IZ[0] % 178)- 63*(IZ[0] // 178)
    if(IX[0] < 0):
        IX[0] = IX[0] + 30269
    if (IY[0] < 0):
        IY[0] = IY[0] + 30307
    if (IZ[0] < 0):
        IZ[0] = IZ[0] + 30323
    inter = (IX[0] / 30269) + (IY[0] / 30307) + (IZ[0] / 30323)
    return(inter - int(inter))




    
def selectionnerF1(alea):
    if alea < 0.3 and alea >=0 :
        return 1
    elif alea <= 0.8 and alea >=0.3:
        return 2
    elif alea <= 0.9 and alea >0.8:
        return 3
    elif alea <= 0.95 and alea >0.9:
        return 4
    elif alea <= 0.98 and alea > 0.95:
        return 5
    else :
        return 6
#---------------------
def selectionnerF2(alea):
    if alea < 0.1 and alea >=0 :
        return 2
    elif alea <0.3 and alea >=0.1:
        return 4
    elif alea <= 0.7 and alea >=0.3:
        return 6
    elif alea <= 0.9 and alea >0.7:
        return 8
    else :
        return 10
#-----------------------
def selectionnerF3(alea):
    if alea < 0.2 and alea >=0 :
        return 1
    elif alea <= 0.6 and alea >=0.2:
        return 2
    elif alea <= 0.85 and alea >0.6:
        return 3
    else:
        return 4

def Planifier(ref, type,calendrier, F):
    calendrier.append([ref,type,F])
    
def selectionner(calendrier):
    mindate=calendrier[0][2]
    index=0
    for i in range(len(calendrier)):
        if(mindate > calendrier[i][2]):
            mindate = calendrier[i][2]
            index = i
    client=[calendrier[index][0],calendrier[index][1],calendrier[index][2]]
    calendrier.remove(calendrier[index])
    return(client)  
    
def findclient(clients,client):
    n = len(clients)
    for i in range(n):
        if (clients[i][0]==client[0]):
            clients[i][2]=client[2]-clients[i][2]  #(Ts) ou (Ta)  
    return clients
#------------------------
def avg(clients):
    n = len(clients)
    j=0
    for i in range(n):
        j=j+clients[i][2] #H de FM

    return j/n
#-----------------
def avgAttente1(clients, TFS):
    j=0
    n=len(clients)
    for i in range(n-1):
        j=j+clients[i][2] #H de FM
    j=j/TFS
    return j
    
def arrive(ref, NCE, NCP,i,LQ,H,calendrier,IX,IY,IZ,clients):
    if (LQ[0]<=1):
        NCE[0] = NCE[0]  + 1
        Planifier(ref,'FM',calendrier,H+selectionnerF2(alea(IX,IY,IZ)))#planifier finmagasinage
        clients.append([i[0],'A',H])
    else: #au plus un client ds la file
        NCP[0]=NCP[0]+1 
    i[0]+=1
    DA = H+selectionnerF1(alea(IX,IY,IZ))
    if(DA<=720):
        Planifier(i[0],'A',calendrier,DA)

def finmagasinage(ref, File,C1, C2, LQ,H,calendrier,ClientsQ,TC1,TC2,IX,IY,IZ,QfileIntervall):
    if(C1[0]==0 or C2[0]==0):
        alea2 = selectionnerF3(alea(IX,IY,IZ))
        if(C1[0]==0):
            C1[0]=ref
            TC1.append([ref,'FM',H]) #delta(T)= H + selectionnerF3(alea) - H
            TC1[0] = TC1[0] + alea2
        else:
            C2[0]=ref
            TC2.append([ref,'FM',H]) #delta(T)= H + selectionnerF3(alea) - H
            TC2[0] = TC2[0] + alea2 #delta(T)= H + selectionnerF3(alea) - H
        Planifier(ref,'FP',calendrier,H+alea2)
    else:
            LQ[0]+=1
            File.append(ref)
            QfileIntervall.append([ref,[H]])
            ClientsQ.append([ref,'FM',H])




def finpaiment(ref, LQ, File, C1, C2,H,calendrier,TC1,TC2,ClientsQ,IX,IY,IZ,QfileIntervall):
    client2 = [ref,'FP',H]
    if(LQ[0]==0):
        if(C1[0]==ref):
            C1[0]=0   
        else:
            C2[0]=0             
    else:
        alea2 = selectionnerF3(alea(IX,IY,IZ))
        J=File[0]
        File.remove(J)
        
        client=[J,'FM',H]
        findFileClient(QfileIntervall,client)
        ClientsQ = findclient(ClientsQ,client)
        LQ[0]-=1
        if(C1[0]==ref):
            C1[0]=J
            
            TC1[0] = TC1[0] + alea2 
            TC1.append(client2)
        else:
            C2[0]=J
            
            TC2[0] = TC2[0] + alea2
            TC2.append(client2)
        Planifier(J,'FP',calendrier,H+alea2)

#-------------
def findLQ(QfileIntervall,interval):
    for j in range(len(interval)):
        for k in range(len(QfileIntervall)):
            if QfileIntervall[k][1][0]<= interval[j][0] and QfileIntervall[k][1][1]>interval[j][0]: #[QfileIntervall[k][1][0] ; QfileIntervall[k][1][1][ => [interval[j][0],+=1]
                interval[j][1] = interval[j][1] + 1



def findFileClient(ClientsQinf,client):
    test = 0
    for j in range(len(ClientsQinf)):
        if ClientsQinf[j][0] == client[0]:
            ClientsQinf[j][1].append(client[2])
#---------




def main(IX1, IY1,IZ1,pt):
    IX=[int(float(IX1))]
    IY=[int(float(IY1))]
    IZ=[int(float(IZ1))]
    x=np.linspace(1,40,num=40)
    y=[]
    z=[]
    KJ = []
    tfs=[]
    tsmoy=[]
    tatmoy=[]
    tauc1moy=[]
    tauc2moy=[]
    ratio11=[]
    ratio22=[]
    MoyJ = [0,0,0,0,0,0,0,0,0]
    carreNCP = [0]
    for j in range(40): #simulation 40 jours
        H=0
        i=[1]
        LQ=[0]
        NCP=[0]
        NCE=[0]
        C1=[0]
        C2=[0]
        QfileIntervall = []
        
        File = []
        clients = [] #pour calculer TSmoy
        ClientsQ =[] #pour calculer TATmoy
        TC1=[0]
        TC2=[0]
        IX[0]=IX[0]+j*5
        IY[0]=IY[0]+j*5
        IZ[0]=IZ[0]+j*5
        
        calendrier = [[1,'A',H+selectionnerF1(alea(IX,IY,IZ))]]
        while (calendrier!=[]):
            client = selectionner(calendrier)
            H = client[2] #maj
            if client[1] == 'A':
                arrive(client[0], NCE, NCP,i,LQ,H,calendrier,IX,IY,IZ,clients)
            elif client[1] == 'FM':
                finmagasinage(client[0], File,C1, C2, LQ,H,calendrier,ClientsQ,TC1,TC2,IX,IY,IZ,QfileIntervall)
            else:
                clients = findclient(clients,client)
                finpaiment(client[0], LQ, File, C1, C2,H,calendrier,TC1,TC2,ClientsQ,IX,IY,IZ,QfileIntervall)
        TFS = H
        interval = []
        for k in range(TFS):
            interval.append([k,0])
        findLQ(QfileIntervall,interval)
        ratio1 = 0
        ratio2 = 0
        for k in range(TFS):
            if interval[k][1]>1:
                ratio2 = ratio2 + 1
            else:
                ratio1 = ratio1 + 1
        ratio1 /= TFS
        ratio2 /= TFS
        TSmoy=avg(clients)#tempsSejour
        TATmoy=avgAttente1(ClientsQ,NCE[0])
        TauC1 = (TC1[0]/TFS)*100
        TauC2 = (TC2[0]/TFS)*100
        y.append(NCE[0])
        z.append(NCP[0])
        tfs.append(TFS)
        tsmoy.append(TSmoy)
        tatmoy.append(TATmoy)
        tauc1moy.append(TauC1)
        tauc2moy.append(TauC2)
        ratio11.append(ratio1)
        ratio22.append(ratio2)
        carreNCP[0] = carreNCP[0] + np.square(NCP[0])
        MoyJ=[MoyJ[0]+NCE[0]/40,MoyJ[1]+NCP[0]/40,MoyJ[2]+TFS/40,MoyJ[3]+TSmoy/40,MoyJ[4]+TATmoy/40,MoyJ[5]+TauC1/40,MoyJ[6]+TauC2/40,MoyJ[7]+ratio1/40,MoyJ[8]+ratio2/40]
        KJ.append([j+1,NCE[0],NCP[0],TFS,TSmoy,TATmoy,TauC1,TauC2,ratio1,ratio2])
    NCPbar = MoyJ[1]
    print("la moyenne des NCP :","%.4f" % NCPbar) ##stocker
    S = np.sqrt(1/39*(carreNCP[0]-40*np.square(NCPbar)))
    IC=[NCPbar - 1.96*(S/np.sqrt(40)),NCPbar + 1.96*(S/np.sqrt(40))]
    print("lintervalle de confiance :",'[',"%.4f" % IC[0],"%.4f" % IC[1],']')
    NCPm=[]
    NCEm=[]
    TFSm=[]
    TSMOy=[]
    TATMOy=[]
    TAUc1=[]
    TAUc2=[]
    RATIo11=[]
    RATIo22=[]
    for j in range(40):
        NCPm.append(MoyJ[1])
        NCEm.append(MoyJ[0])
        TFSm.append(MoyJ[2])
        TSMOy.append(MoyJ[3])
        TATMOy.append(MoyJ[4])
        TAUc1.append(MoyJ[5])
        TAUc2.append(MoyJ[6])
        RATIo11.append(MoyJ[7])
        RATIo22.append(MoyJ[8])
    KJ.append(MoyJ)
    KJ[40].insert(0,'La moyenne')
    
    fig, axs = plt.subplots(3,3)
#plot NCE
    axs[0][0].plot(x,y)
    axs[0][0].set_title('Evolution du NCE par jour')
    axs[0][0].plot(x,NCEm,'g')
    axs[0][0].set(xlabel='jours', ylabel='NCE')
#plot NCP
    axs[0][1].plot(x,z, 'tab:orange')
    axs[0][1].plot(x,NCPm,'g')
    axs[0][1].set_title('Evolution du NCP par jour')
    axs[0][1].set(xlabel='jours', ylabel='NCP')
#plot TFS
    axs[0][2].plot(x,tfs, 'tab:purple')
    axs[0][2].plot(x,TFSm,'g')
    axs[0][2].set_title('Evolution du TFS par jour')
    axs[0][2].set(xlabel='jours', ylabel='TFS')
#plot TSMOY
    axs[1][0].plot(x,tsmoy, 'tab:red')
    axs[1][0].plot(x,TSMOy,'g')
    axs[1][0].set_title('Evolution du TSMOY par jour')
    axs[1][0].set(xlabel='jours', ylabel='TSMOY')
#plot TATMOY
    axs[1][1].plot(x,tatmoy, 'tab:pink')
    axs[1][1].plot(x,TATMOy,'g')
    axs[1][1].set_title('Evolution du TATMOY par jour')
    axs[1][1].set(xlabel='jours', ylabel='TATMOY')
#plot TAUC1
    axs[1][2].plot(x,tauc1moy, 'tab:brown')
    axs[1][2].plot(x,TAUc1,'g')
    axs[1][2].set_title('Evolution du TAUC1 par jour')
    axs[1][2].set(xlabel='jours', ylabel='TAUC1')
#plot TAUC2
    axs[2][0].plot(x,tauc2moy, 'tab:cyan')
    axs[2][0].plot(x,TAUc2,'g')
    axs[2][0].set_title('Evolution du TAUC2 par jour')
    axs[2][0].set(xlabel='jours', ylabel='TAUC2')
#plot RATIO1
    axs[2][1].plot(x,ratio11, 'tab:olive')
    axs[2][1].plot(x,RATIo11,'g')
    axs[2][1].set_title('Evolution du RATIO1 par jour')
    axs[2][1].set(xlabel='jours', ylabel='RATIO1')
#plot RATIO2
    axs[2][2].plot(x,ratio22, 'tab:gray')
    axs[2][2].plot(x,RATIo22,'g')
    axs[2][2].set_title('Evolution du RATIO2 par jour')
    axs[2][2].set(xlabel='jours', ylabel='RATIO2')

    if pt==1:
        plt.show()
    return KJ
    
    
