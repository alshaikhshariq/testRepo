import Levenshtein

def fuzzy_map_headers(source_headers, target_headers):
    mapping = {}
    used_targets = set()

    for src in source_headers:
        best_match = None
        best_score = float('inf')

        for tgt in target_headers:
            if tgt in used_targets:
                continue
            score = Levenshtein.distance(src.lower(), tgt.lower())
            if score < best_score:
                best_score = score
                best_match = tgt

        if best_match:
            mapping[src] = best_match
            used_targets.add(best_match)

    return mapping
