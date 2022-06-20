if __name__ != "__main__":
    from app.random_value import RandomValue
    from gui.widgets.my_widgets.exception import CustomValueError


class RSA:

    def encrypt(self, n: int, e: int, content: str) -> str:

        outputContent = ""
        # RUN ORIGINAL FILE
        for M in content:
            C = self.__QuickMod(ord(M), e, n)
            outputContent += str(C) + ' '

        return outputContent[:-1] # retorna sem o último caractere

    def encryptChar(self, n: int, e: int, M: str) -> str:
        C = self.__QuickMod(ord(M), e, n)
        return C

    def decrypt(self, p: int, q: int, e: int, content: str) -> str:
        
        outputContent = ""
        # GETS THE INVERSE KEY
        d = self.__inverse(e, (p - 1) * (q - 1))

        # RUN ENCRYPTED MESSAGE        
        contentValues = content.split()
        for C in contentValues:
           
            try:
                M = self.__QuickMod(int(C), d, p * q)
            except ValueError:                
                raise CustomValueError("Value error raised")

            # convert int to bytes type and write in output file
            print(M)
            outputContent += chr(M)

        return outputContent

    def decryptChar(self, p: int, q: int, e: int, C: str) -> str:

        d = self.__inverse(e, (p - 1) * (q - 1))
        M = self.__QuickMod(int(C), d, p * q)
        return str(M)

    def generateKeys(self, security_level):      

        # dic = {0: [3 , 5],
        #        1: [5 , 7],
        #        2: [7 , 11],
        #        3: [11, 13]
        # }
        # start = 11 ** dic[security_level][0]
        # end = 11 ** dic[security_level][1]

        random = RandomValue()
        self.key_P = random.getPrime(security_level)
        self.key_Q = random.getPrime(security_level)
        self.key_E = random.exp(self.key_P, self.key_Q)
        self.key_D = self.__inverse(self.key_E, (self.key_P - 1) * (self.key_Q - 1))

        # print("P: ", self.key_P)
        # print("Q: ", self.key_Q)
        # print("N: ", self.get_key_N())
        # print("E: ", self.key_E)
        # print("D: ", self.key_D)

    def get_public_key(self) -> str:

        public = ""        
        for char in str(self.get_key_N()):
            public += chr(int(char) + 162)
        public += chr(187)
        for char in str(self.get_key_E()):
            public += chr(int(char) + 162) 
        return public        

    def get_private_key(self) -> str:
        private = ""        
        for char in str(self.get_key_P()):
            private += chr(int(char) + 162)
        private += chr(187)
        for char in str(self.get_key_Q()):
            private += chr(int(char) + 162)
        private += chr(187)
        for char in str(self.get_key_E()):
            private += chr(int(char) + 162)
        
        return private         

    def get_key_P(self) -> str:
        return str(self.key_P)
    
    def get_key_Q(self) -> str:
        return str(self.key_Q)

    def get_key_N(self) -> str:
        return str(self.key_P * self.key_Q)
    
    def get_key_E(self) -> str:
        return str(self.key_E)
    
    def get_key_D(self) -> str:
        return str(self.key_D)

    @staticmethod
    def __QuickMod(base, exp, n):
        """retorna o resultado de base^exp mod(n) através da exponenciação rápida"""

        result = 1
        while exp > 0:
            if exp & 1:
                result = (result * base) % n
            
            base = (base ** 2) % n
            exp = exp >> 1

        return result

    @classmethod
    def __linearOperation(cls, a, b, mdc, i):
        """retorna os coeficientes lineares da
        expressão: mdc(a, b) = sa + tb = 1"""
        t = -(a // b)
        r = a % b

        mdc.append([1, a, t, b])

        if r == 1:
            return mdc

        # recebe a ultima operação do mdc cujo resultado é 1 ( mdc(a, b) = sa + tb = 1 )
        inverseLine = cls.__linearOperation(b, r, mdc, i + 1)

        s = inverseLine[i][0]
        t = inverseLine[i][2]
        inverseLine[i - 1][0] *= t
        inverseLine[i - 1][2] *= t
        inverseLine[i - 1][2] += s

        inverseLine.remove(inverseLine[i])
        return inverseLine  # retorna a última lista com o inverso incluso

    @staticmethod
    def XMDC(a,b):
        
        prevu, u = 1, 0; prevv, v = 0, 1 
        
        while b != 0:
            q = a//b
            u, prevu = prevu - q*u, u
            v, prevv = prevv - q*v, v
            a, b = b, a % b
   
        return a, prevu, prevv

    def __inverse(self, e, φ):
        """recebe e, φ; retorna inverso de e ≡ 1 mod(φ)"""
        inverseLine = self.__linearOperation(e, φ, [], 1)
        inverse = inverseLine[0][0]
        # inverseLine = self.XMDC(e, φ)
        # inverse = inverseLine[1]

        if inverse < 0:
            return inverse + φ
        if inverse > φ:
            return inverse % φ
        else:
            return inverse


if __name__== "__main__":
    pass
