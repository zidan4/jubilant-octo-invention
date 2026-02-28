def bing_menu(self,event):
  
  # grab the details of what the user clicked
  http_traffic = self.context.getSelectedMessages()
  print "%d requests highlighted" % len(http_traffic)
  for traffic in http_traffic:
  http_service = traffic.getHttpService()
  host
  = http_service.getHost()
  print "User selected host: %s" % host
  self.bing_search(host)
  return
  
def bing_search(self,host):
# check if we have an IP or hostname
  is_ip = re.match("[0-9]+(?:\.[0-9]+){3}", host)
  
  if is_ip:
    ip_address = host
    domain = False
  else:
    ip_address = socket.gethostbyname(host)
    domain = True
  
  bing_query_string = "'ip:%s'" % ip_address
  self.bing_query(bing_query_string)
  
  if domain:
    bing_query_string = "'domain:%s'" % host
    self.bing_query(bing_query_string)
