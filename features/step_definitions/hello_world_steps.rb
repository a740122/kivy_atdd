require 'json'
require 'httparty'
require 'recursive-open-struct'
require 'rspec-expectations'

def search_by_id (root, id)
  root.children.each do |child|
    return child if child.id == id
    return search_by_id(child, id) 
  end
end

Given(/^the application is running$/) do

end

Then(/^I should see "(.*?)"$/) do |message|
  response = HTTParty.get('http://localhost:5000/ui')
  ui_tree = JSON.parse(response.body)
  ui_tree = RecursiveOpenStruct.new(ui_tree, recurse_over_arrays: true)
  label = search_by_id(ui_tree, 'mylabel')
  label.value.should == message
end
