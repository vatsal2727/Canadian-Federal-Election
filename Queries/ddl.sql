# Create Table Query

CREATE TABLE vote_share(
	ridingNumber integer NOT NULL PRIMARY KEY ,
	ridingNameEnglish VARCHAR (100) UNIQUE NOT NULL,
	ridingNameFrench VARCHAR (100) UNIQUE NOT NULL,
	totalVotes integer NOT NULL,	
	turnout NUMERIC (5, 2),
	conservativeVoteShare Numeric (5,2),
	liberalVoteShare Numeric (5,2),
	NDPVoteShare Numeric (5,2),
	greenVoteShare Numeric (5,2),
	blocQuebecoisVoteShare Numeric (5,2),
	peoplePartyVoteShare Numeric (5,2)
);

CREATE TABLE candidates
(
	ridingNumber integer NOT NULL,
	CONCandidateName VARCHAR (100),
	LIBCandidateName VARCHAR (100),
	GRNCandidateName VARCHAR (100),
	NDPCandidateName VARCHAR (100),
	BQCandidateName VARCHAR (100),
	PPCCandidateName VARCHAR (100),
	PRIMARY KEY (ridingNumber),
	CONSTRAINT ridingNumber_fk FOREIGN KEY (ridingNumber)
	REFERENCES vote_share (ridingNumber) MATCH SIMPLE
	ON UPDATE NO ACTION ON DELETE NO ACTION
);
