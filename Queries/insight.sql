# Find the riding with biggest win margin
SELECT 
 ridingNumber, ridingNameEnglish, GREATEST(conservativeVoteShare, liberalVoteShare, NDPVoteShare, greenVoteShare, blocQuebecoisVoteShare,peoplePartyVoteShare) AS BiggestMargin 
FROM 
  candidates.vote_share
Order BY 
  BiggestMargin DESC
LIMIT 1;
