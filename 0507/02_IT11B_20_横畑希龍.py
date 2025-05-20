#数値のみを受け付けるinput関数
def inputNumber(prompt):
  while True:
    try:
      return float(input(prompt))
    except ValueError:
      print("😠:文字列じゃなくて数値を入れてね!!")

#演算子のみを受け付けるinput関数
def inputOperator(prompt):
  while True:
    opt=input(prompt)
    if   opt=="+":return opt 
    elif opt=="-":return opt
    elif opt=="*":return opt
    elif opt=="/":return opt
    elif opt=="=":return opt
    else:print("😵: 四則演算しかできないよ~~")

#四則演算を行う関数
def calc(num1,opt,num2):
  if   opt=="+":return num1+num2
  elif opt=="-":return num1-num2
  elif opt=="*":return num1*num2
  elif opt=="/":return num1/num2

def caluculator():
  result=inputNumber("数値を入力してください: ")
  #「=」が入力されるまで四則演算を継続
  while True:
    opt=inputOperator("演算子を入力してください(+,-,*,/,=): ")
    if opt=="=":
      print(f"計算結果は{result}です。")
      break
    num=inputNumber("数値を入力してください: ")

    #ゼロ除算をするかの確認
    while opt=="/" and num==0:
      isDivideZero=input("😨: 本当に0で割り算してもいいですか?? [y/n] ")
      if(isDivideZero=="y"):
        print("計算結果は「解なし(未定義)」です。")
        return
      else: num=inputNumber("もう一度数値を入力してください!!: ")

    result=calc(result,opt,num)
caluculator()
