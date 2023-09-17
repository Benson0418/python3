Roman={1000:'M',900:'CM',500:'D',400:'CD',100:'C',90:'XC',50:'L',40:'XL',10:'X',9:'IX',5:'V',4:'IV',1:'I'}
Int={'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1}
def intToRoman(num:int) -> str:
    if num==0:
        return "ZERO"
    result=""
    for k,v in Roman.items():
        while num>=k:
            num-=k
            result=result+v
    return result
def RomanToInt(nums:str) -> int:
    result=0
    for i in range(len(nums)-1):
        if Int[nums[i]]<Int[nums[i+1]]:
            result-=Int[nums[i]]
        else:
            result+=Int[nums[i]]
    result+=Int[nums[-1]]
    return result
    
while True:
    inputw=input()
    if inputw=='#':
        break
    a,b=inputw.split()
    Ra,Rb=RomanToInt(a),RomanToInt(b)
    print(intToRoman(abs(Ra-Rb)))
