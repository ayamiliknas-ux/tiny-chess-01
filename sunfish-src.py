# tiny-chess-01 entry: packed sunfish fork (GPL-3.0, https://github.com/thomasahle/sunfish)
# pruned for size: history heuristic, TT eviction and deadline plumbing removed; node-capped search kept.
#!/bin/sh
v='pnbrqk';u=enumerate;t=tuple;n='B';m='N';l=ord;k=int;j=next;i=range;b=len;a=min;U=False;S='.';R='Q';Q='R';P=print;M=max;L='P';K=abs;I=None;G=True;F='K';import time as c;from itertools import count;from collections import namedtuple as d;N={L:100,m:280,n:320,Q:479,R:929,F:60000};E={L:(0,0,0,0,0,0,0,0,78,83,86,73,102,82,85,90,7,29,21,44,40,31,44,7,-17,16,-2,15,14,0,15,-13,-26,3,10,9,6,1,0,-23,-22,9,5,-11,-10,-2,3,-19,-31,8,-7,-37,-36,-14,3,-31,0,0,0,0,0,0,0,0),m:(-66,-53,-75,-75,-10,-55,-58,-70,-3,-6,100,-36,4,62,-4,-14,10,67,1,74,73,27,62,-2,24,24,45,37,33,41,25,17,-1,5,31,21,22,35,2,0,-18,10,13,22,18,15,11,-14,-23,-15,2,0,2,0,-23,-20,-74,-23,-26,-24,-19,-35,-22,-69),n:(-59,-78,-82,-76,-23,-107,-37,-50,-11,20,35,-42,-39,31,2,-22,-9,39,-32,41,52,-10,28,-14,25,17,20,34,26,25,15,10,13,10,17,23,17,16,0,7,14,25,24,15,8,25,20,15,19,20,11,6,7,6,20,16,-7,2,-15,-12,-14,-15,-10,-10),Q:(35,29,33,4,37,33,56,50,55,29,56,67,55,62,34,60,19,35,28,33,45,27,25,15,0,5,16,13,18,-4,-9,-6,-28,-35,-16,-21,-13,-29,-46,-30,-42,-28,-42,-25,-25,-35,-26,-46,-53,-38,-31,-26,-29,-43,-44,-53,-30,-24,-18,5,-2,-18,-31,-32),R:(6,1,-8,-104,69,24,88,26,14,32,60,-10,20,76,57,24,-2,43,32,60,72,63,43,2,1,-16,22,17,25,20,-13,-6,-14,-15,-2,-5,-1,-10,-20,-22,-30,-6,-13,-11,-16,-11,-16,-27,-36,-18,0,-19,-15,-15,-21,-38,-39,-30,-31,-13,-31,-36,-34,-42),F:(4,54,47,-99,-99,60,83,-62,-32,10,55,56,56,55,10,3,-62,12,-57,44,-67,28,37,-31,-55,50,11,-4,-19,13,0,-49,-55,-43,-52,-28,-51,-47,-8,-50,-47,-42,-43,-79,-64,-32,-29,-32,-4,3,-14,-50,-57,-18,13,4,17,30,-3,-14,6,-1,40,18)}
for(V,x)in E.items():y=lambda row:(0,)+t(A+N[V]for A in row)+(0,);E[V]=sum((y(x[A*8:A*8+8])for A in i(8)),());E[V]=(0,)*20+E[V]+(0,)*20
z,A0=E[F],t(N[F]+70-10*(K(2*(A//10)-11)+K(2*(A%10)-9))for A in i(120));J,W,X,Y=91,98,21,28;A1='         \n         \n rnbqkbnr\n pppppppp\n ........\n ........\n ........\n ........\n PPPPPPPP\n RNBQKBNR\n         \n         \n';A,B,D,C=-10,1,10,-1;A2={L:(A,A+A,A+C,A+B),m:(A+A+B,B+A+B,B+D+B,D+D+B,D+D+C,C+D+C,C+A+C,A+A+C),n:(A+B,D+B,D+C,A+C),Q:(A,B,D,C),R:(A,B,D,C,A+B,D+B,D+C,A+C),F:(A,B,D,C,A+B,D+B,D+C,A+C)};Z=N[F]-13*N[R];H=N[F]+10*N[R];o=36;A3=180;A4=70;e=15;A5=-200;f=200;T=d('Move','i j prom')
class g(d('Position','board score wc bc ep kp')):
	def gen_moves(E):
		for(G,I)in u(E.board):
			if I not in'PNBRQK':continue
			for H in A2[I]:
				for D in count(G+H,H):
					M=E.board[D]
					if M in' \nPNBRQK':break
					if I==L:
						if H in(A,A+A)and M!=S:break
						if H==A+A and(G<J+A or E.board[G+A]!=S):break
						if H in(A+C,A+B)and M==S and D!=E.ep and K(D-E.kp)>1:break
						if X<=D<=Y:yield from(T(G,D,A)for A in'NBRQ');break
					yield T(G,D,'')
					if I in'PNK'or M in v:break
					if G==J and E.board[D+B]==F and E.wc[0]:yield T(D+B,D+C,'')
					if G==W and E.board[D+C]==F and E.wc[1]:yield T(D+C,D+B,'')
	def rotate(A,nullmove=U):B=nullmove;return g(A.board[::-1].swapcase(),-A.score,A.bc,A.wc,119-A.ep if A.ep and not B else 0,119-A.kp if A.kp and not B else 0)
	def move(G,move):
		E,C,R=move;H=lambda board,i,p:board[:i]+p+board[i+1:];O,V,B,I,M,P,N=G.board[E],G.board[C],G.board,G.wc,G.bc,0,0;T=G.score+G.value(move);B=H(B,C,B[E]);B=H(B,E,S);I=I[0]and E!=J,I[1]and E!=W;M=M[0]and C!=Y,M[1]and C!=X
		if O==F:
			I=U,U
			if K(C-E)==2:N=(E+C)//2;B=H(B,J if C<E else W,S);B=H(B,N,Q)
		if O==L:
			if X<=C<=Y:B=H(B,C,R)
			if C-E==2*A:P=E+A
			if C==G.ep:B=H(B,C+D,S)
		return g(B,T,I,M,P,N).rotate()
	def value(G,move):
		C,A,M=move;H,I=G.board[C],G.board[A];B=E[H][A]-E[H][C]
		if I in v:B+=E[I.upper()][119-A]
		if K(A-G.kp)<2:B+=E[F][119-A]
		if H==F and K(C-A)==2:B+=E[Q][(C+A)//2];B-=E[Q][J if A<C else W]
		if H==L:
			if X<=A<=Y:B+=E[M][A]-E[L][A]
			if A==G.ep:B+=E[L][119-(A+D)]
		return B
	def king_capture(A):return j((B for B in A.gen_moves()if A.board[B.j]=='k'or K(B.j-A.kp)<2),I)
class q(Exception):0
h=d('Entry','lower upper')
class A6:
	def __init__(A):A.tp_score,A.tp_move={},{};A.nodes=0
	def bound(C,pos,gamma,depth,root=U):
		P=root;D=gamma;B=depth;A=pos;C.nodes+=1
		B=M(B,0)
		if A.score<=-Z:return-H
		if not P:
			J=C.tp_score.get((A,B),h(-H,H))
			if J.lower>=D:return J.lower
			if J.upper<D:return J.upper
		Q=C.tp_move.get(A);S=lambda v:H if B>4 or v>=Z else A.score+v+M(B-1,0)*A3
		def X():
			if 2<B<6 and V:yield(I,I)
			if B==0:yield(I,I)
			if Q and((C:=A.value(Q))>=o or B)and S(C)>=D:yield(C,Q)
			yield from sorted(((E,C)for C in A.gen_moves()if(E:=A.value(C))>=o or B),reverse=G)
		T=K(A.score)<750 and any(B in A.board for B in'RBNQ');V=not P and T;W=A.score+A5;Y=T and B>=6 and-C.bound(A.rotate(nullmove=G),1-W,B-7)>=W;E,O=-H,U
		for(R,L)in X():
			if L is I and B==0:F=A.score
			elif L is I:
				if(N:=A.score+e)>=D:
					F=a(N,-C.bound(A.rotate(nullmove=G),1-D,B-4))
					if F>=D and(d:=A.king_capture()):L,F,O=d,H,G
				else:F=N
			elif R>=Z:F,O=H,G
			else:
				if(N:=S(R))<D:E=M(E,N);break
				f=B-1-(V and B>=7 and R<A4)-k(Y);F=a(N,-C.bound(A.move(L),1-D,f));O|=F>-H
			E=M(E,F)
			if E>=D:
				if L is not I and B:
					C.tp_move[A]=L
				break
		if B and not O and all(A.move(B).king_capture()for B in A.gen_moves()):g=M(1-H,-Z-B*e);E=g if A.rotate(nullmove=G).king_capture()else 0
		if not P:C.tp_score[A,B]=h(E,J.upper)if E>=D else h(J.lower,E)
		return E
	def search(A,history):
		K=history;A.nodes,A.tp_score=0,{};D=A.root=K[-1];E[F]=z if R in D.board and'q'in D.board else A0;B=0
		for L in i(1,1000):
			I,J=1-H,H
			while I<J-e:
				C=A.bound(D,B,L,root=G)
				if C>=B:I=C
				if C<B:J=C
				yield(L,B,C,A.tp_move.get(D));B=(I+J+1)//2
def r(c):return J+l(c[0])-l('a')-10*(k(c[1])-1)
def s(i):return chr((i-J)%10+l('a'))+str(1-(i-J)//10)
import json as zzjson, urllib.request as zzurl, os as zzos, sys as zzsys
zzbase = zzos.environ['MAKEFUN_ENV_URL']
def zzpost(zp, zb):
	zzr = zzurl.urlopen(zzurl.Request(zzbase + zp, data=zzjson.dumps(zb).encode()))
	return zzjson.load(zzr)
def zzbest(zzmoves, zzlegal):
	zzs = A6()
	zzmirror = len(zzmoves) % 2 == 1
	zzhist = [g(A1, 0, (G, G), (G, G), 0, 0)]
	for zzk, zu in enumerate(zzmoves):
		zzfi, zzti = r(zu[:2]), r(zu[2:4])
		if zzk % 2 == 1: zzfi, zzti = 119 - zzfi, 119 - zzti
		zzhist.append(zzhist[-1].move(T(zzfi, zzti, zu[4:].upper())))
	def zzconv(zu):
		zzfi = r(zu[:2]); zzti = r(zu[2:4])
		if zzmirror: zzfi, zzti = 119 - zzfi, 119 - zzti
		return T(zzfi, zzti, zu[4:].upper())
	zzallowed = [zzconv(zu) for zu in zzlegal]
	zzpick = None
	zzcap = 50000
	try:
		for (zzsc, zzmv, zzd2, zzq2) in zzs.search(zzhist):
			if zzq2 in zzallowed: zzpick = zzq2
			if zzs.nodes >= zzcap: break
	except q: pass
	if zzpick is None: zzpick = zzallowed[0]
	zzfi, zzti = zzpick.i, zzpick.j
	if zzmirror: zzfi, zzti = 119 - zzfi, 119 - zzti
	return s(zzfi) + s(zzti) + (zzpick.prom or '').lower()
zzf = zzpost('/game', {})
while zzf.get('status') != 'done':
	if zzf.get('status') == 'your_move':
		zzf = zzpost('/move', {'game': zzf['game'], 'move': zzbest(zzf['moves'], zzf['legal_moves'])})
	else:
		print('game %s: %s by %s' % (zzf.get('game'), zzf.get('outcome'), zzf.get('reason')), file=zzsys.stderr)
		zzf = zzpost('/game', {})
print('RESULT', zzf.get('wins'), zzf.get('draws'), zzf.get('losses'), file=zzsys.stderr)
