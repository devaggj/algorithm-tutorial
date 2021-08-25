"""
class, instance, 매개변수 self에 관해서

class 안의 메소드에 self를 매개변수로 명시해야하지만, 
class를 직접 이용하여 메소드에 접근할 경우에는 self가 없어도 정상 실행 가능함
"""

class PythonSelf:
    
    def sayHello1():
        print('Hello without self')
    
    def sayHello2(self):
        print('Hello with self')
        print('id: ', id(self))




if __name__ == '__main__':
    """
    1: class의 instance 생성 후 instance를 통해 메소드 실행할 경우
    instance에서 자신을 argument로 전달하므로 sayHello1는 에러생성, sayHello2는 정상 실행
    """
    p = PythonSelf()
    p.sayHello()    # error
    p.sayHello2()   
    
    """
    2: instance 생성이 아닌 class에서 직접 메소드를 선택해 사용할 경우 
    sayHello1 정상 실행, sayHello2는 class 자신을 argument로 전달해야 정상 실행
    """
    PythonSelf.sayHello1()  
    PythonSelf.sayHello2()  # error
    PythonSelf.sayHello2(PythonSelf)    # class를 직접 self의 인자값으로 전달
    
    """
    3. 
    """
    PythonSelf().sayHello1()    # instance를 생성한 것과 같으므로 error
    PythonSelf().sayHello2()
