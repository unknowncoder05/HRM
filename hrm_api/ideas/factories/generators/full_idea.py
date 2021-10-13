from hrm_api.ideas.factories import IdeaFactory
from hrm_api.utils.models import save_save

def idea_generator(distribution:list): 
    """
    distribution: [
        (
            user: User,
            ideas: int,
            original_thinker: Profile
        )
    , ... ]
    """
    ideas = []
    for user_indx, user_distribution in enumerate(distribution):
        for idea_indx in range(user_distribution[1]):
            idea = IdeaFactory(
                created_by=user_distribution[0].profile,
                original_thinker=user_distribution[2],
                #name=str(user_indx)+str(idea_indx)
                )
            #save_save(idea.feed)
            #save_save(idea)
            ideas.append(idea)
    
    return ideas