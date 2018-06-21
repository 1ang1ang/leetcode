# -*- encoding= utf-8 -*-

# 题目url: https://leetcode.com/problems/subdomain-visit-count/description/

class Solution:
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        dic={}
        for d in cpdomains:
            count,domain =str(d).split(" ")
            count = int(count)
            domain = str(domain)
            domainSplit = domain.split(".")
            for i in range(int(len(domainSplit))):
                name = ".".join(domainSplit[i:])
                dic[name] = dic.get(name,0) + count
        return ["{} {}".format(str(v) ,str(k)) for k, v in dic.items()]
print(Solution.subdomainVisits(Solution,["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]))