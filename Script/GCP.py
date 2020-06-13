#!/usr/bin/env python
# coding: utf-8
import requests
import json
from google.cloud import bigquery

def vote_share():
    try:
        client = bigquery.Client()
        dataset_id = 'candidates'
        candidate_table_id = 'candidatesInfo'
        vote_share_table_id = 'vote_share'
        
        candidate_table_ref = client.dataset(dataset_id).table(candidate_table_id)
        vote_share_table_ref = client.dataset(dataset_id).table(vote_share_table_id)

        candidate_table = client.get_table(candidate_table_ref)
        vote_share_table = client.get_table(vote_share_table_ref)

        print ("successfully Connected!")

        # Using Candidates_For_Riding API to get data 
        for x in range(1,339):
            # storing the API response into variable
            response = requests.get("https://electionsapi.cp.org/api/federal2019/Candidates_For_Riding?ridingnumber=" + str(x))
            jsonData = response.json()

            # Default value of vote share and Candidate name is NULL in case if that party did not have any candidate for that riding
            CONVoteShare=LIBVoteShare=GRNVoteShare=NDPVoteShare=BQVoteShare=PPCVoteShare = 0.0
            CONCandidateName=LIBCandidateName=GRNCandidateName=NDPCandidateName=BQCandidateName=PPCCandidateName=""

            ridingNumber = response.json()[0]['RidingNumber']
            ridingNameEnglish = response.json()[0]['RidingName_En']
            ridingNameFrench = response.json()[0]['RidingName_Fr']
            # Counting turnout using total votes and total voters
            totalVotes = response.json()[0]['TotalVotes']
            totalVoters = response.json()[0]['TotalVoters']
            turnout = round((totalVotes/totalVoters)*100,2)

            # fetching Candidate Names and their vote share in respective riding
            for data in jsonData:
                firstName = data['First']
                if data['PartyShortName_En']=="CON":
                    CONVoteShare = round((((data['Votes'])/totalVotes)*100),2)    
                    CONCandidateName = firstName
                if data['PartyShortName_En']=="LIB":
                    LIBVoteShare = round((((data['Votes'])/totalVotes)*100),2)
                    LIBCandidateName = firstName
                if data['PartyShortName_En']=="GRN":
                    GRNVoteShare = round((((data['Votes'])/totalVotes)*100),2)
                    GRNCandidateName = firstName
                if data['PartyShortName_En']=="NDP":
                    NDPVoteShare = round((((data['Votes'])/totalVotes)*100),2)
                    NDPCandidateName = firstName
                if data['PartyShortName_En']=="BQ":
                    BQVoteShare = round((((data['Votes'])/totalVotes)*100),2)
                    BQCandidateName = firstName
                if data['PartyShortName_En']=="PPC":
                    PPCVoteShare = round((((data['Votes'])/totalVotes)*100),2)
                    PPCCandidateName = firstName

            # Prepring data and query for "vote_share" table
            voteShareRecord = [(ridingNumber,ridingNameEnglish,ridingNameFrench,totalVotes,turnout,CONVoteShare,LIBVoteShare,GRNVoteShare,NDPVoteShare,BQVoteShare,PPCVoteShare)]
            #insert_data_query = """ INSERT INTO vote_share (ridingnumber, ridingnameenglish, ridingnamefrench, totalvotes, turnout, conservativevoteshare, liberalvoteshare, greenvoteshare, ndpvoteshare, blocquebecoisvoteshare, peoplepartyvoteshare) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

            # Prepring data and query for Candidates table
            candidateRecord = [(ridingNumber,CONCandidateName,LIBCandidateName,GRNCandidateName,NDPCandidateName,BQCandidateName,PPCCandidateName)]
            #insert_candidate_query = """ INSERT INTO candidates (ridingnumber, CONCandidateName, LIBCandidateName, GRNCandidateName, NDPCandidateName, BQCandidateName, PPCCandidateName) VALUES (%s,%s,%s,%s,%s,%s,%s)"""

            # Inserting data into "vote_share" and "candidates" table
            #cursor.execute(insert_data_query, record)
            #cursor.execute(table, candidateRecord)
            insert_vote_share = client.insert_rows(vote_share_table, voteShareRecord)
            insert_candidates = client.insert_rows(candidate_table, candidateRecord)
            
            #connection.commit()

        print("Records successfully inserted into table!")
        
    # if unable to connect with database except will occur
    except:
        print ("Error while connecting GCP")

    # once data is succesfully uploaded, connection close
    finally:
        assert insert_candidates == []
        assert insert_vote_share == []
        print("Done!")

if __name__ == '__main__':
    vote_share()    
