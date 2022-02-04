import dns.resolver


class Resolver:

    def __init__(self, ns):
        self.resolver = dns.resolver.Resolver()
        self.resolver.nameservers = [ns] 
        self.types = ['NS', 'TXT', 'ANY']
    
    def is_vulnerable(self):
        passed = 0
        for t in self.types:
            try:
                result = self.resolver.resolve('google.com', t)
                if len([x.to_text() for x in result]) > 0:
                    passed += 1
            except:
                pass
        if passed >= 1:
            return True
        
        return False
        