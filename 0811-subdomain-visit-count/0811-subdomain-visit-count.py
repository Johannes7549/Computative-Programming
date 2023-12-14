class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
               
        d = {}
        for cpdomain in cpdomains:
            count, domain = cpdomain.split()
            count = int(count)
            subdomains = domain.split('.')
            for i in range(len(subdomains)):
                subdomain = '.'.join(subdomains[i:])
                d[subdomain] = d.get(subdomain, 0) + count
        return [str(count) + ' ' + domain for domain, count in d.items()]
            