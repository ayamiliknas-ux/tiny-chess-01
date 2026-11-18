def uci_sq(zzc):
	"""Square name from a sunfish 120-board index."""
	return chr((zzc - 91) % 10 + ord('a')) + str(1 - (zzc - 91) // 10)


def uci_idx(zzc):
	"""Sunfish 120-board index from a square name."""
	return 91 + ord(zzc[0]) - ord('a') - 10 * (int(zzc[1]) - 1)


def env_post(zzpath, zzbody):
	"""POST a JSON body to the env and return its JSON answer."""
	zzreq = zzurl.Request(zzbase + zzpath, data=zzjson.dumps(zzbody).encode())
	with zzurl.urlopen(zzreq) as zzres:
		return zzjson.load(zzres)


def build_history(zzmoves):
	"""Rebuild the position history from the env's move list."""
	zzhist = [g(A1, 0, (G, G), (G, G), 0, 0)]
	for zzk, zu in enumerate(zzmoves):
		zzfi, zzti = uci_idx(zu[:2]), uci_idx(zu[2:4])
		if zzk % 2 == 1:
			zzfi, zzti = 119 - zzfi, 119 - zzti
		zzhist.append(zzhist[-1].move(T(zzfi, zzti, zu[4:].upper())))
	return zzhist


def to_engine(zzu):
	"""Legal UCI move to a sunfish Move in the entry's orientation."""
	zzfi, zzti = uci_idx(zu[:2]), uci_idx(zu[2:4])
	if zzmirror:
		zzfi, zzti = 119 - zzfi, 119 - zzti
	return T(zzfi, zzti, zu[4:].upper())


def count_seen(zzhist):
	"""How often each position (board, castling, ep) has appeared."""
	zzseen = {}
	for zzp in zzhist:
		zzkey = (zzp.board, zzp.wc, zzp.bc, zzp.ep)
		zzseen[zzkey] = zzseen.get(zzkey, 0) + 1
	return zzseen


def repeats(zzm):
	"""A move is vetoed when it repeats a seen position (draw risk)."""
	zzc = zzhist[-1].move(zzm)
	zzkey = (zzc.board, zzc.wc, zzc.bc, zzc.ep)
	return zzseen.get(zzkey, 0) >= 1


def best_move(zzmoves, zzlegal):
	"""Iterative MTD search under a node cap, repetition-vetoed."""
	global zzmirror, zzhist, zzseen
	zzmirror = len(zzmoves) % 2 == 1
	zzhist = build_history(zzmoves)
	zzseen = count_seen(zzhist)
	zzallowed = [to_engine(zu) for zu in zzlegal]
	zzpick = None
	zzcap = 20000
	zzs = A6()
	try:
		for (zzsc, zzmv, zzd2, zzq2) in zzs.search(zzhist):
			if zzq2 in zzallowed:
				zzpick = zzq2
			if zzs.nodes >= zzcap:
				break
	except q:
		pass
	if zzpick is not None and repeats(zzpick):
		zzpick = None
	if zzpick is None:
		for zzc in zzallowed:
			if not repeats(zzc):
				zzpick = zzc
				break
	if zzpick is None:
		zzpick = zzallowed[0]
	zzfi, zzti = zzpick.i, zzpick.j
	if zzmirror:
		zzfi, zzti = 119 - zzfi, 119 - zzti
	return uci_sq(zzfi) + uci_sq(zzti) + (zzpick.prom or '').lower()


zzgame = env_post('/game', {})
while zzgame.get('status') != 'done':
	if zzgame.get('status') == 'your_move':
		zzmv = best_move(zzgame['moves'], zzgame['legal_moves'])
		zzgame = env_post('/move', {'game': zzgame['game'], 'move': zzmv})
	else:
		zzline = 'game %s: %s by %s' % (zzgame.get('game'), zzgame.get('outcome'), zzgame.get('reason'))
		print(zzline, file=zzsys.stderr)
		zzgame = env_post('/game', {})
zzres = 'RESULT %s %s %s' % (zzgame.get('wins'), zzgame.get('draws'), zzgame.get('losses'))
print(zzres, file=zzsys.stderr)
