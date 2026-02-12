def checkmate(board):
    try:
        if not board or not isinstance(board, str):
            print("Error")
            return

        rows = board.splitlines()
        size = len(rows)

        if size == 0 or any(len(row) != size for row in rows):
            print("Error")
            return

        king_pos = None
        for r in range(size):
            for c in range(size):
                if rows[r][c] == 'K':
                    if king_pos is not None:  
                        print("Error")
                        return
                    king_pos = (r, c)

        if king_pos is None:
            print("Error")
            return

        kr, kc = king_pos

        straight_dirs = [(-1,0),(1,0),(0,-1),(0,1)]
        diag_dirs = [(-1,-1),(-1,1),(1,-1),(1,1)]

        for dr, dc in straight_dirs:
            r, c = kr + dr, kc + dc
            while 0 <= r < size and 0 <= c < size:
                piece = rows[r][c]
                if piece != '.':
                    if piece in ('R', 'Q'):
                        print("Success")
                        return
                    break
                r += dr
                c += dc

        for dr, dc in diag_dirs:
            r, c = kr + dr, kc + dc
            while 0 <= r < size and 0 <= c < size:
                piece = rows[r][c]
                if piece != '.':
                    if piece in ('B', 'Q'):
                        print("Success")
                        return
                    break
                r += dr
                c += dc

        pawn_attacks = [(1,-1), (1,1)]
        for dr, dc in pawn_attacks:
            r, c = kr + dr, kc + dc
            if 0 <= r < size and 0 <= c < size:
                if rows[r][c] == 'P':
                    print("Success")
                    return

        print("Fail")

    except Exception:
        print("Error")
