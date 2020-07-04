import praw

#reddit api login
reddit = praw.Reddit(client_id = 'k_jOB-RRBSIsxA',
                    client_secret = '	IAqcUz409vr9IIZNmzoOlaj_zG0',
                    username = 'amal25',
                    password = 'newredditbotPolls',
                    user_agent = 'pollsbot by /u/amal25')

# the subreddits you want your bot to live on
subreddit = reddit.subreddit('politics')

# phrase to activate the bot
keyphrase = '!todaysPoll'

# looks for phrase and replies accordingly
for comment in subreddit.steam.comments():
    if keyphrase in comment.body:
        word = comment.body.replace(keyphrase, '')
        try:
            # we get the data from another python file (webscraping)
            theReply = "| Dates | Pollster | Sample | Approval | Results | Disapproval | Net Results \n"
            spacing = ":-- | :--: | :--: | :--: | :--: | :--: | :--: | --: \n"
            
            # the below is the format for reply
            comment.reply('')
            print('posted')
        except:
            print("You are requesting this too frequently.")



