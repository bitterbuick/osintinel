# Bug Report
## Description
Error fetching profile for user @mountain_goats: 403 Forbidden.

## Steps to Reproduce

1. Run the CLI tool with the Twitter command:
```bash
python src/cli/cli.py twitter @mountain_goats'
```
2. Observe the following error message:
<PRE>
Error fetching profile for user @@mountain_goats: 403 Forbidden
When authenticating requests to the Twitter API v2 endpoints, you must use keys and tokens from a Twitter developer App that is attached to a Project. You can create a project via the developer portal.
</PRE>

## Expected Behavior

The tool should fetch the Twitter profile information without a 403 Forbidden error.

## Actual Behavior

A 403 Forbidden error occurs, indicating an issue with the authentication tokens or the app configuration.

## Troubleshooting Steps Taken
1. Verified that the Twitter Developer App is attached to a project.
2. Checked that the correct API keys and tokens are being used.
3. Added debug prints to verify the bearer token.
4. Updated twitter_scraper.py to use the bearer token correctly.

## Next Steps

- Review the permissions and access levels of the Twitter Developer App.
- Ensure that the app has the required access to the necessary API endpoints.
- Consider reaching out to Twitter Developer Support if the issue persists.

## Additional Information

I'll add this to Kanban later to keep track.

=======
# Bug Repor
## Descriptio
Error fetching profile for user @mountain_goats: 403 Forbidden.

## Steps to Reproduce

Run the CLI tool with the Twitter command:
```bash python src/cli/cli.py twitter @mountain_goats ```

Observe the following error message:
<pre>Error fetching profile for user @@mountain_goats: 403 Forbidden
When authenticating requests to the Twitter API v2 endpoints, you must use keys and tokens from a Twitter developer App that is attached to a Project. You can create a project via the developer portal.
</pre>
## Expected Behavior

The tool should fetch the Twitter profile information without a 403 Forbidden error.

## Actual Behavior

A 403 Forbidden error occurs, indicating an issue with the authentication tokens or the app configuration.

## Troubleshooting Steps Taken
Verified that the Twitter Developer App is attached to a project.
Checked that the correct API keys and tokens are being used.
Added debug prints to verify the bearer token.
Updated twitter_scraper.py to use the bearer token correctly.

## Next Steps

Review the permissions and access levels of the Twitter Developer App.
Ensure that the app has the required access to the necessary API endpoints.
Consider reaching out to Twitter Developer Support if the issue persists.

## Additional Information

I'll add this to Kanban later to keep track.
