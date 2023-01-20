-- **************************************************
--	Setup DDL for sample azure data factory pipeline
--	example used here: 
--  https://www.metadapi.com/Blog/dynamically-invoking-rest-api-with-data-factory
-- ************************************** [sourceCRM]

CREATE TABLE [dbo].[sourceCRM]
(
 [customerId] int IDENTITY (1, 1) NOT NULL ,
 [zipCode]    varchar(5) NOT NULL ,


 CONSTRAINT [PKsourceCRM] PRIMARY KEY CLUSTERED ([customerId] ASC)
);
GO

-- ************************************** [targetCRM]

CREATE TABLE [dbo].[targetCRM]
(
 [customerId]          int NOT NULL ,
 [zipCode]             varchar(5) NOT NULL ,
 [stateName]           varchar(50) NULL ,
 [stateCode]           varchar(2) NULL ,
 [titleCaseCountyName] varchar(50) NULL ,
 [titleCaseCityName]   varchar(50) NOT NULL ,
 [latitude]            decimal(9,6) NULL ,
 [longitude]           decimal(9,6) NULL ,
 [msaCode]             varchar(5) NULL ,
 [msaName]             varchar(100) NULL 

);
GO