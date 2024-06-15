class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        boxes.sort(reverse=True)
        cnt = 0
        warehouse_index = 0
        cur_height = warehouse[0]

        for box in boxes:
            if warehouse_index >= len(warehouse):
                break

            cur_height = min(cur_height, warehouse[warehouse_index])
            if cur_height >= box:
                # can push
                cnt += 1
                warehouse_index += 1

        return cnt
