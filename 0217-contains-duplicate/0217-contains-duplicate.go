func containsDuplicate(nums []int) bool {
    hashmap:=make(map[int]int)
    for _,ele := range nums{
        hashmap[ele]+=1
        if hashmap[ele]>1{
            return true
        }
       
    }
    return false
}