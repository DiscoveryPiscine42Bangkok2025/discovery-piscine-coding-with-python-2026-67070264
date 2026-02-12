def checkmate(board):
    try:
        if not board or not isinstance(board, str):
            print("Error")
            return

        rows = board.splitlines()
        size = len(rows)

        # board must be square
        if size == 0 or any(len(row) != size for row in rows):
            print("Error")
            return

        # find King
        king_pos = None
        for r in range(size):
            for c in range(size):
                if rows[r][c] == 'K':
                    if king_pos is not None:  # more than one king
                        print("Error")
                        return
                    king_pos = (r, c)

        if king_pos is None:
            print("Error")
            return

        kr, kc = king_pos

        # directions for rook & queen (straight)
        straight_dirs = [(-1,0),(1,0),(0,-1),(0,1)]
        # directions for bishop & queen (diagonal)
        diag_dirs = [(-1,-1),(-1,1),(1,-1),(1,1)]

        # check straight lines (R, Q)
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

        # check diagonals (B, Q)
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

        # check pawns (P)
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
