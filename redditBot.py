import praw
from webscrape538 import fivethirtyeight
#reddit api login
reddit = praw.Reddit(client_id = "k_jOB-RRBSIsxA",
                    client_secret = "IAqcUz409vr9IIZNmzoOlaj_zG0",
                    username = 'amal25',
                    password = 'newredditbotPolls',
                    user_agent = 'pollsbot by /u/amal25')
# the subreddits you want your bot to live on
subreddit = reddit.subreddit('politics')

# phrase to activate the bot
keyphrase = '!todaysPoll'

# looks for phrase and replies accordingly
for comment in subreddit.stream.comments():
    if keyphrase in comment.body:
        word = comment.body.replace(keyphrase, '')
        # we get the data from another python file (webscraping)
        if fivethirtyeight():
            theReply = "| Poll Name| Dates | Pollster | Sample | Sample Type | Approval | Disapproval | Net Results |\n"
            spacing = "| :-- | :--: | :--: | :--: | :--: | :--: | :--: | --: |\n"
            endComment = theReply + spacing
            polls = fivethirtyeight()
            for i in polls:
                endComment += i
            # the below is the format for reply
            comment.reply(endComment)
            print('posted the poll!')
        else:
            reply = "no polls at this time"
            comment.reply(reply)
            print('posted - no content')
        # except:
        #     print("You are requesting this too frequently.")



