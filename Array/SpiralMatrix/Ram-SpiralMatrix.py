class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:return []
        srt_rw,end_rw,srt_cl,end_cl=0,len(matrix),0,len(matrix[0])
        result=[]
        while srt_rw<end_rw or srt_cl<end_cl:
            if srt_rw<end_rw:
                for i in range(srt_cl,end_cl): #moving right
                    result.append(matrix[srt_rw][i])
            srt_rw+=1
            if srt_cl<end_cl:
                for i in range(srt_rw,end_rw): #moving down
                    result.append(matrix[i][end_cl-1])
            end_cl-=1
            if srt_rw<end_rw:
                for i in range(end_cl-1,srt_cl-1,-1): #moving left
                    result.append(matrix[end_rw-1][i])
            end_rw-=1
            if srt_cl<end_cl:
                for i in range(end_rw-1,srt_rw-1,-1): #moving up
                    result.append(matrix[i][srt_cl])
            srt_cl+=1

        return result