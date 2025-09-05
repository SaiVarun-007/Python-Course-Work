#Base Class - Instagram Story

class InstagramStory:
    def __init__(self, user):
        self.user = user
        self.story_content = ""
        
    def post_story(self, content):
        self.story_content = content
        return f"{self.user} posted a story: {content}"
    
    
class StoryWithLikes(InstagramStory):
    def __init__(self, user):
        super().__init__(user)
        self.likes()

    def like_story(self):
        self.like +=1
        print(f"Story Liked! Total likes: {self.likes}")