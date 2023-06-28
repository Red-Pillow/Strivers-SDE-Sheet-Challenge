# prob_link: https://www.codingninjas.com/studio/problems/flood-fill-algorithm_8230806?challengeSlug=striver-sde-challenge&leftPanelTab=0

def floodFill(image, sr, sc, color):
    # Write your Code here.
    original = image[sr][sc]
    n = len(image)
    m = len(image[0])

    def dfs(i,j):
        if i>=n or i<0 or j>=m or j<0:
            return
        if image[i][j]==color or image[i][j]!=original:
            return

        if image[i][j]==original:
            image[i][j] = color
            dfs(i-1,j)
            dfs(i,j-1)
            dfs(i+1,j)
            dfs(i,j+1)

    dfs(sr,sc)
    return image