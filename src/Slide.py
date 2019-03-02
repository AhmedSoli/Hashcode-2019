class Slide:

	def __init__(self,*argv):

		if len(argv) == 1:
			self.id = argv[0]['id']
			self.tags = argv[0]['tags']
			self.tag_ids = argv[0]['tag_ids']
		elif len(argv) == 2:
			self.id = (argv[0]['id'],argv[1]['id'])
			self.tag_ids = argv[0]['tag_ids'] | argv[1]['tag_ids']
			self.tags = len(self.tag_ids)

		self.slide = {'id':self.id,'tags':self.tags,'tag_ids':self.tag_ids}

	def __getitem__(self,item):
		return self.slide[item]

	def __str__(self):
		return("ID {} tags {} tag_ids {}".format(self.id,self.tags,self.tag_ids))
