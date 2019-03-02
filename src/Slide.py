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
