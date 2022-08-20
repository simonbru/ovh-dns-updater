# Should missing IP address being considered as error (Depend on the ISP, internet box settings...)?
# In case a required IP cannot be obtained, the script will send an email and stop without updating anything. 
# If, for any reason, IPv4 or IPv6 address cannot be obtained and if it is not protected by this list, the corresponding records will be deleted for all hosts.
ip_versions_required = [4] # MUST not be empty. Can be [4],[6] or [4,6] 

default_ttl =  600  # seconds
# ttl = how long will a DNS server cache the value before checking it at the Registrar. Longer value yields faster name resolution most of the time, but less frequent updates

# list of hosts (=subdomain.domain.tld) to update, each a dictionnary with at least "domain" and "subdomain" defined
hosts = [
        {
            "domain": "mydomain.tld", # Required
            "subdomain": "www", # Required. Explicit subdomain or empty string "" (for @) or "*" for wildcard
            #"ipv6": any_value_except_False # Optional : maintain corresponding record, when possible
            "ipv4": False, #explicitly disable modifiying ipv4 (A) records, even if public IPV4 exists (a possibly erroneous record would be left as-is)
            #"ttl": 60 # optional : if 'ttl' in specified in host, overrides the global default value 
        },
        {
            "domain": "otherdomain.tld",
            "subdomain": ""
            # 'ipv4' and 'ipv6' are not listed : automatically maintain any/both records, according to availability
        }
    ]

checkDNS_interval_hrs = 12.1 # when the saved IP addresses are old, check the DNS record, even if the addresses did not change